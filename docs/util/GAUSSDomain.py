# -*- coding: utf-8 -*-
"""
    ~~~~~~~~~~~~~~~~~~~~~

    The GAUSS domain, based on Python (leaving as much in-tact as possible)

    :copyright: Copyright 2007-2019 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from __future__ import annotations

import ast
import builtins
import inspect
import re
import token
import typing
from inspect import Parameter
from typing import Any, Iterable, Iterator, List, NamedTuple, Tuple, cast

from docutils import nodes
from docutils.nodes import Element, Node
from docutils.parsers.rst import directives
from docutils.parsers.rst.states import Inliner

from sphinx import addnodes
from sphinx.addnodes import desc_signature, pending_xref, pending_xref_condition
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, Index, IndexEntry, ObjType
from sphinx.environment import BuildEnvironment
from sphinx.locale import _, __
from sphinx.pycode.parser import Token, TokenProcessor
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.docfields import Field, GroupedField, TypedField
from sphinx.util.docutils import SphinxDirective
from sphinx.util.inspect import signature_from_str
from sphinx.util.nodes import (
    find_pending_xref_condition,
    make_id,
    make_refnode,
    nested_parse_with_titles,
)
from sphinx.util.typing import OptionSpec, TextlikeNode
from GAUSSHTMLTranslator import desc_returnlist, desc_return

if False:
    # For type annotation
    from typing import Any, Dict, Iterable, Iterator, List, Tuple, Union  # NOQA
    from sphinx.application import Sphinx  # NOQA
    from sphinx.builders import Builder  # NOQA
    from sphinx.environment import BuildEnvironment  # NOQA

logger = logging.getLogger(__name__)


# REs for Python signatures
py_sig_re = re.compile(
    r'''^ (?:
          \{? \s*(.*?)\s*?\}?  # returns
          \s*=\s*
          )?
          ([\w.]*\.)?            # prefix/class? name
          (\w+)  \s*             # thing name
          (?: \(\s*(.*)\s*\)     # optional: arguments
          )? $                   # and nothing more
          ''', re.VERBOSE)


pairindextypes = {
    'module': 'module',
    'keyword': 'keyword',
    'operator': 'operator',
    'object': 'object',
    'exception': 'exception',
    'statement': 'statement',
    'builtin': 'built-in function',
}


class ObjectEntry(NamedTuple):
    docname: str
    node_id: str
    objtype: str
    aliased: bool


class ModuleEntry(NamedTuple):
    docname: str
    node_id: str
    synopsis: str
    platform: str
    deprecated: bool


def parse_reftarget(reftarget: str, suppress_prefix: bool = False,
                    ) -> tuple[str, str, str, bool]:
    """Parse a type string and return (reftype, reftarget, title, refspecific flag)"""
    refspecific = False
    if reftarget.startswith('.'):
        reftarget = reftarget[1:]
        title = reftarget
        refspecific = True
    elif reftarget.startswith('~'):
        reftarget = reftarget[1:]
        title = reftarget.split('.')[-1]
    elif suppress_prefix:
        title = reftarget.split('.')[-1]
    elif reftarget.startswith('typing.'):
        title = reftarget[7:]
    else:
        title = reftarget

    if reftarget == 'None' or reftarget.startswith('typing.'):
        # typing module provides non-class types.  Obj reference is good to refer them.
        reftype = 'obj'
    else:
        reftype = 'class'

    return reftype, reftarget, title, refspecific


def _pseudo_parse_generic(signode, arglist, desc_listtype, desc_type):
    # type: (addnodes.desc_signature, unicode) -> None
    """ "Parse" a list of returns separated by commas.
    """
    genericlist = desc_listtype()
    stack = [genericlist]
    try:
        for argument in arglist.split(','):
            argument = argument.strip()
            ends_open = ends_close = 0
            while argument.startswith('['):
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                argument = argument[1:].strip()
            while argument.startswith(']'):
                stack.pop()
                argument = argument[1:].strip()
            while argument.endswith(']') and not argument.endswith('[]'):
                ends_close += 1
                argument = argument[:-1].strip()
            while argument.endswith('['):
                ends_open += 1
                argument = argument[:-1].strip()
            if argument:
                stack[-1] += desc_type(argument, argument)
            while ends_open:
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                ends_open -= 1
            while ends_close:
                stack.pop()
                ends_close -= 1
        if len(stack) != 1:
            raise IndexError
    except IndexError:
        # if there are too few or too many elements on the stack, just give up
        # and treat the whole argument list as one argument, discarding the
        # already partially populated returnlist node
        signode += desc_listtype()
        signode[-1] += desc_type(arglist, arglist)
    else:
        signode += genericlist


def _pseudo_parse_arglist(signode, arglist):
    _pseudo_parse_generic(signode, arglist,
                          addnodes.desc_parameterlist,
                          addnodes.desc_parameter)


def _pseudo_parse_returns(signode, returns):
    _pseudo_parse_generic(signode, returns,
                          desc_returnlist,
                          desc_return)


# This override allows our inline type specifiers to behave like :class: link
# when it comes to handling "." and "~" prefixes.
class PyXrefMixin:
    def make_xref(
        self,
        rolename: str,
        domain: str,
        target: str,
        innernode: type[TextlikeNode] = nodes.emphasis,
        contnode: Node | None = None,
        env: BuildEnvironment | None = None,
        inliner: Inliner | None = None,
        location: Node | None = None,
    ) -> Node:
        # we use inliner=None to make sure we get the old behaviour with a single
        # pending_xref node
        result = super().make_xref(rolename, domain, target,  # type: ignore
                                   innernode, contnode,
                                   env, inliner=None, location=None)
        if isinstance(result, pending_xref):
            result['refspecific'] = True
            result['gauss:module'] = env.ref_context.get('gauss:module')
            result['gauss:class'] = env.ref_context.get('gauss:class')

            reftype, reftarget, reftitle, _ = parse_reftarget(target)
            if reftarget != reftitle:
                result['reftype'] = reftype
                result['reftarget'] = reftarget

                result.clear()
                result += innernode(reftitle, reftitle)
            elif env.config.python_use_unqualified_type_names:
                children = result.children
                result.clear()

                shortname = target.split('.')[-1]
                textnode = innernode('', shortname)
                contnodes = [pending_xref_condition('', '', textnode, condition='resolved'),
                             pending_xref_condition('', '', *children, condition='*')]
                result.extend(contnodes)

        return result

    def make_xrefs(
        self,
        rolename: str,
        domain: str,
        target: str,
        innernode: type[TextlikeNode] = nodes.emphasis,
        contnode: Node | None = None,
        env: BuildEnvironment | None = None,
        inliner: Inliner | None = None,
        location: Node | None = None,
    ) -> list[Node]:
        delims = r'(\s*[\[\]\(\),](?:\s*o[rf]\s)?\s*|\s+o[rf]\s+|\s*\|\s*|\.\.\.)'
        delims_re = re.compile(delims)
        sub_targets = re.split(delims, target)

        split_contnode = bool(contnode and contnode.astext() == target)

        in_literal = False
        results = []
        for sub_target in filter(None, sub_targets):
            if split_contnode:
                contnode = nodes.Text(sub_target)

            if in_literal or delims_re.match(sub_target):
                results.append(contnode or innernode(sub_target, sub_target))
            else:
                results.append(self.make_xref(rolename, domain, sub_target,
                                              innernode, contnode, env, inliner, location))

            if sub_target in ('Literal', 'typing.Literal', '~typing.Literal'):
                in_literal = True

        return results


class PyField(PyXrefMixin, Field):
    pass


class PyGroupedField(PyXrefMixin, GroupedField):
    pass


class PyTypedField(PyXrefMixin, TypedField):
    pass


class PyObject(ObjectDescription):
    """
    Description of a general Python object.

    :cvar allow_nesting: Class is an object that allows for nested namespaces
    :vartype allow_nesting: bool
    """
    option_spec: OptionSpec = {
        'noindex': directives.flag,
        'noindexentry': directives.flag,
        'nocontentsentry': directives.flag,
        'single-line-parameter-list': directives.flag,
        'single-line-type-parameter-list': directives.flag,
        'module': directives.unchanged,
        'canonical': directives.unchanged,
        'annotation': directives.unchanged,
    }

    doc_field_types = [
        PyTypedField('parameter', label=_('Parameters'),
                     names=('param', 'parameter', 'arg', 'argument',
                            'keyword', 'kwarg', 'kwparam'),
                     typerolename='class', typenames=('paramtype', 'type'),
                     can_collapse=True),
        PyTypedField('variable', label=_('Variables'),
                     names=('var', 'ivar', 'cvar'),
                     typerolename='class', typenames=('vartype',),
                     can_collapse=True),
        PyGroupedField('exceptions', label=_('Raises'), rolename='exc',
                       names=('raises', 'raise', 'exception', 'except'),
                       can_collapse=True),
        PyTypedField('returnvalue', label=_('Returns'),
                     names=('returns', 'return'),
                     typerolename='class', typenames=('rtype',),
                     can_collapse=True),
        # Field('returnvalue', label=_('Returns'), has_arg=False,
        #       names=('returns', 'return')),
        # PyField('returntype', label=_('Return type'), has_arg=False,
        #         names=('rtype',), bodyrolename='class'),
    ]

    allow_nesting = False

    def get_signature_prefix(self, sig):
        # type: (unicode) -> unicode
        """May return a prefix to put before the object name in the
        signature.
        """
        return []

    def needs_arglist(self):
        # type: () -> bool
        """May return true if an empty argument list is to be generated even if
        the document contains none.
        """
        return False

    def handle_signature(self, sig, signode):
        # type: (unicode, addnodes.desc_signature) -> Tuple[unicode, unicode]
        """Transform a Python signature into RST nodes.

        Return (fully qualified name of the thing, classname if any).

        If inside a class, the current class name is handled intelligently:
        * it is stripped from the displayed name if present
        * it is added to the full name (return value) if not present
        """
        m = py_sig_re.match(sig)
        if m is None:
            raise ValueError
        retann, name_prefix, name, arglist = m.groups()

        # determine module and class name (if applicable), as well as full name
        modname = self.options.get(
            'module', self.env.ref_context.get('gauss:module'))
        classname = self.env.ref_context.get('gauss:class')
        if classname:
            add_module = False
            if name_prefix and name_prefix.startswith(classname):
                fullname = name_prefix + name
                # class name is given again in the signature
                name_prefix = name_prefix[len(classname):].lstrip('.')
            elif name_prefix:
                # class name is given in the signature, but different
                # (shouldn't happen)
                fullname = classname + '.' + name_prefix + name
            else:
                # class name is not given in the signature
                fullname = classname + '.' + name
        else:
            add_module = True
            if name_prefix:
                classname = name_prefix.rstrip('.')
                fullname = name_prefix + name
            else:
                classname = ''
                fullname = name

        signode['module'] = modname
        signode['class'] = classname
        signode['fullname'] = fullname

        max_len = (self.env.config.python_maximum_signature_line_length
                   or self.env.config.maximum_signature_line_length
                   or 0)


        # determine if the function arguments (without its type parameters)
        # should be formatted on a multiline or not by removing the width of
        # the type parameters list (if any)
        sig_len = len(sig)
        tp_list_span = m.span(3)
        multi_line_parameter_list = (
            'single-line-parameter-list' not in self.options
            and (sig_len - (tp_list_span[1] - tp_list_span[0])) > max_len > 0
        )

        # determine whether the type parameter list must be wrapped or not
        arglist_span = m.span(4)
        multi_line_type_parameter_list = (
            'single-line-type-parameter-list' not in self.options
            and (sig_len - (arglist_span[1] - arglist_span[0])) > max_len > 0
        )

        sig_prefix = self.get_signature_prefix(sig)
        if sig_prefix:
            if type(sig_prefix) is str:
                raise TypeError(
                    "Python directive method get_signature_prefix()"
                    " must return a list of nodes."
                    f" Return value was '{sig_prefix}'.")
            signode += addnodes.desc_annotation(str(sig_prefix), '', *sig_prefix)
            #signode += addnodes.desc_annotation(sig_prefix, sig_prefix)

        if retann:
            _pseudo_parse_returns(signode, retann)
            # signode += addnodes.desc_returns(retann, '', *children) # (v7.x)
            # signode += addnodes.desc_returns(retann, retann) # v1.8.5 (original)

        if name_prefix:
            signode += addnodes.desc_addname(name_prefix, name_prefix)
        # exceptions are a special case, since they are documented in the
        # 'exceptions' module.
        elif add_module and self.env.config.add_module_names:
            modname = self.options.get(
                'module', self.env.ref_context.get('gauss:module'))
            if modname and modname != 'exceptions':
                nodetext = modname + '.'
                signode += addnodes.desc_addname(nodetext, nodetext)

        signode += addnodes.desc_name(name, name)
        if arglist:
            _pseudo_parse_arglist(signode, arglist)
        else:
            if self.needs_arglist():
                # for callables, add an empty parameter list
                signode += addnodes.desc_parameterlist()

        anno = self.options.get('annotation')
        if anno:
            signode += addnodes.desc_annotation(' ' + anno, '',
                                                addnodes.desc_sig_space(),
                                                nodes.Text(anno))

        return fullname, name_prefix

    def get_index_text(self, modname, name):
        # type: (unicode, unicode) -> unicode
        """Return the text for the index entry of the object."""
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls: tuple[str, str], sig: str,
                             signode: desc_signature) -> None:
        modname = self.options.get('module', self.env.ref_context.get('gauss:module'))
        fullname = (modname + '.' if modname else '') + name_cls[0]
        node_id = make_id(self.env, self.state.document, '', fullname)
        signode['ids'].append(node_id)
        self.state.document.note_explicit_target(signode)

        domain = cast(GAUSSDomain, self.env.get_domain('gauss'))
        domain.note_object(fullname, self.objtype, node_id, location=signode)

        canonical_name = self.options.get('canonical')
        if canonical_name:
            domain.note_object(canonical_name, self.objtype, node_id, aliased=True,
                               location=signode)

        if 'noindexentry' not in self.options:
            indextext = self.get_index_text(modname, name_cls)
            if indextext:
                self.indexnode['entries'].append(('single', indextext, node_id, '', None))

    def before_content(self):
        # type: () -> None
        """Handle object nesting before content

        :gauss:class:`PyObject` represents Python language constructs. For
        constructs that are nestable, such as a Python classes, this method will
        build up a stack of the nesting heirarchy so that it can be later
        de-nested correctly, in :gauss:meth:`after_content`.

        For constructs that aren't nestable, the stack is bypassed, and instead
        only the most recent object is tracked. This object prefix name will be
        removed with :gauss:meth:`after_content`.
        """
        prefix = None
        if self.names:
            # fullname and name_prefix come from the `handle_signature` method.
            # fullname represents the full object name that is constructed using
            # object nesting and explicit prefixes. `name_prefix` is the
            # explicit prefix given in a signature
            (fullname, name_prefix) = self.names[-1]
            if self.allow_nesting:
                prefix = fullname
            elif name_prefix:
                prefix = name_prefix.strip('.')
        if prefix:
            self.env.ref_context['gauss:class'] = prefix
            if self.allow_nesting:
                classes = self.env.ref_context.setdefault('gauss:classes', [])
                classes.append(prefix)
        if 'module' in self.options:
            modules = self.env.ref_context.setdefault('gauss:modules', [])
            modules.append(self.env.ref_context.get('gauss:module'))
            self.env.ref_context['gauss:module'] = self.options['module']

    def after_content(self):
        # type: () -> None
        """Handle object de-nesting after content

        If this class is a nestable object, removing the last nested class prefix
        ends further nesting in the object.

        If this class is not a nestable object, the list of classes should not
        be altered as we didn't affect the nesting levels in
        :gauss:meth:`before_content`.
        """
        classes = self.env.ref_context.setdefault('gauss:classes', [])
        if self.allow_nesting:
            try:
                classes.pop()
            except IndexError:
                pass
        self.env.ref_context['gauss:class'] = (classes[-1] if len(classes) > 0
                                            else None)
        if 'module' in self.options:
            modules = self.env.ref_context.setdefault('gauss:modules', [])
            if modules:
                self.env.ref_context['gauss:module'] = modules.pop()
            else:
                self.env.ref_context.pop('gauss:module')

    def _toc_entry_name(self, sig_node: desc_signature) -> str:
        if not sig_node.get('_toc_parts'):
            return ''

        config = self.env.app.config
        objtype = sig_node.parent.get('objtype')
        if config.add_function_parentheses and objtype in {'function', 'method'}:
            parens = '()'
        else:
            parens = ''
        *parents, name = sig_node['_toc_parts']
        if config.toc_object_entries_show_parents == 'domain':
            return sig_node.get('fullname', name) + parens
        if config.toc_object_entries_show_parents == 'hide':
            return name + parens
        if config.toc_object_entries_show_parents == 'all':
            return '.'.join(parents + [name + parens])
        return ''


class PyFunction(PyObject):
    """Description of a function."""

    option_spec: OptionSpec = PyObject.option_spec.copy()
    option_spec.update({
        'async': directives.flag,
    })

    def get_signature_prefix(self, sig: str) -> list[nodes.Node]:
        if 'async' in self.options:
            return [addnodes.desc_sig_keyword('', 'async'),
                    addnodes.desc_sig_space()]
        else:
            return []

    def needs_arglist(self) -> bool:
        return True

    def add_target_and_index(self, name_cls: tuple[str, str], sig: str,
                             signode: desc_signature) -> None:
        super().add_target_and_index(name_cls, sig, signode)
        if 'noindexentry' not in self.options:
            modname = self.options.get('module', self.env.ref_context.get('gauss:module'))
            node_id = signode['ids'][0]

            name, cls = name_cls
            if modname:
                text = _('%s() (in module %s)') % (name, modname)
                self.indexnode['entries'].append(('single', text, node_id, '', None))
            else:
                text = f'built-in function; {name}()'
                self.indexnode['entries'].append(('pair', text, node_id, '', None))

    def get_index_text(self, modname: str, name_cls: tuple[str, str]) -> str | None:
        # add index in own add_target_and_index() instead.
        return None


class PyDecoratorFunction(PyFunction):
    """Description of a decorator."""

    def run(self) -> list[Node]:
        # a decorator function is a function after all
        self.name = 'gauss:function'
        return super().run()

    def handle_signature(self, sig: str, signode: desc_signature) -> tuple[str, str]:
        ret = super().handle_signature(sig, signode)
        signode.insert(0, addnodes.desc_addname('@', '@'))
        return ret

    def needs_arglist(self) -> bool:
        return False


class PyVariable(PyObject):
    """Description of a variable."""

    option_spec: OptionSpec = PyObject.option_spec.copy()
    option_spec.update({
        'type': directives.unchanged,
        'value': directives.unchanged,
    })

    def handle_signature(self, sig: str, signode: desc_signature) -> tuple[str, str]:
        fullname, prefix = super().handle_signature(sig, signode)

        typ = self.options.get('type')
        if typ:
            annotations = _parse_annotation(typ, self.env)
            signode += addnodes.desc_annotation(typ, '',
                                                addnodes.desc_sig_punctuation('', ':'),
                                                addnodes.desc_sig_space(), *annotations)

        value = self.options.get('value')
        if value:
            signode += addnodes.desc_annotation(value, '',
                                                addnodes.desc_sig_space(),
                                                addnodes.desc_sig_punctuation('', '='),
                                                addnodes.desc_sig_space(),
                                                nodes.Text(value))

        return fullname, prefix

    def get_index_text(self, modname: str, name_cls: tuple[str, str]) -> str:
        name, cls = name_cls
        if modname:
            return _('%s (in module %s)') % (name, modname)
        else:
            return _('%s (built-in variable)') % name


class PyClasslike(PyObject):
    """
    Description of a class-like object (classes, interfaces, exceptions).
    """

    option_spec: OptionSpec = PyObject.option_spec.copy()
    option_spec.update({
        'final': directives.flag,
    })

    allow_nesting = True

    def get_signature_prefix(self, sig: str) -> list[nodes.Node]:
        if 'final' in self.options:
            return [nodes.Text('final'), addnodes.desc_sig_space(),
                    nodes.Text(self.objtype), addnodes.desc_sig_space()]
        else:
            return [nodes.Text(self.objtype), addnodes.desc_sig_space()]

    def get_index_text(self, modname: str, name_cls: tuple[str, str]) -> str:
        if self.objtype == 'class':
            if not modname:
                return _('%s (built-in class)') % name_cls[0]
            return _('%s (class in %s)') % (name_cls[0], modname)
        elif self.objtype == 'exception':
            return name_cls[0]
        else:
            return ''


class PyMethod(PyObject):
    """Description of a method."""

    option_spec: OptionSpec = PyObject.option_spec.copy()
    option_spec.update({
        'abstractmethod': directives.flag,
        'async': directives.flag,
        'classmethod': directives.flag,
        'final': directives.flag,
        'staticmethod': directives.flag,
    })

    def needs_arglist(self) -> bool:
        return True

    def get_signature_prefix(self, sig: str) -> list[nodes.Node]:
        prefix: list[nodes.Node] = []
        if 'final' in self.options:
            prefix.append(nodes.Text('final'))
            prefix.append(addnodes.desc_sig_space())
        if 'abstractmethod' in self.options:
            prefix.append(nodes.Text('abstract'))
            prefix.append(addnodes.desc_sig_space())
        if 'async' in self.options:
            prefix.append(nodes.Text('async'))
            prefix.append(addnodes.desc_sig_space())
        if 'classmethod' in self.options:
            prefix.append(nodes.Text('classmethod'))
            prefix.append(addnodes.desc_sig_space())
        if 'staticmethod' in self.options:
            prefix.append(nodes.Text('static'))
            prefix.append(addnodes.desc_sig_space())
        return prefix

    def get_index_text(self, modname: str, name_cls: tuple[str, str]) -> str:
        name, cls = name_cls
        try:
            clsname, methname = name.rsplit('.', 1)
            if modname and self.env.config.add_module_names:
                clsname = '.'.join([modname, clsname])
        except ValueError:
            if modname:
                return _('%s() (in module %s)') % (name, modname)
            else:
                return '%s()' % name

        if 'classmethod' in self.options:
            return _('%s() (%s class method)') % (methname, clsname)
        elif 'staticmethod' in self.options:
            return _('%s() (%s static method)') % (methname, clsname)
        else:
            return _('%s() (%s method)') % (methname, clsname)


class PyClassMethod(PyMethod):
    """Description of a classmethod."""

    option_spec: OptionSpec = PyObject.option_spec.copy()

    def run(self) -> list[Node]:
        self.name = 'gauss:method'
        self.options['classmethod'] = True

        return super().run()


class PyStaticMethod(PyMethod):
    """Description of a staticmethod."""

    option_spec: OptionSpec = PyObject.option_spec.copy()

    def run(self) -> list[Node]:
        self.name = 'gauss:method'
        self.options['staticmethod'] = True

        return super().run()


class PyDecoratorMethod(PyMethod):
    """Description of a decoratormethod."""

    def run(self) -> list[Node]:
        self.name = 'gauss:method'
        return super().run()

    def handle_signature(self, sig: str, signode: desc_signature) -> tuple[str, str]:
        ret = super().handle_signature(sig, signode)
        signode.insert(0, addnodes.desc_addname('@', '@'))
        return ret

    def needs_arglist(self) -> bool:
        return False


class PyAttribute(PyObject):
    """Description of an attribute."""

    option_spec: OptionSpec = PyObject.option_spec.copy()
    option_spec.update({
        'type': directives.unchanged,
        'value': directives.unchanged,
    })

    def handle_signature(self, sig: str, signode: desc_signature) -> tuple[str, str]:
        fullname, prefix = super().handle_signature(sig, signode)

        typ = self.options.get('type')
        if typ:
            annotations = _parse_annotation(typ, self.env)
            signode += addnodes.desc_annotation(typ, '',
                                                addnodes.desc_sig_punctuation('', ':'),
                                                addnodes.desc_sig_space(),
                                                *annotations)

        value = self.options.get('value')
        if value:
            signode += addnodes.desc_annotation(value, '',
                                                addnodes.desc_sig_space(),
                                                addnodes.desc_sig_punctuation('', '='),
                                                addnodes.desc_sig_space(),
                                                nodes.Text(value))

        return fullname, prefix

    def get_index_text(self, modname: str, name_cls: tuple[str, str]) -> str:
        name, cls = name_cls
        try:
            clsname, attrname = name.rsplit('.', 1)
            if modname and self.env.config.add_module_names:
                clsname = '.'.join([modname, clsname])
        except ValueError:
            if modname:
                return _('%s (in module %s)') % (name, modname)
            else:
                return name

        return _('%s (%s attribute)') % (attrname, clsname)


class PyProperty(PyObject):
    """Description of an attribute."""

    option_spec = PyObject.option_spec.copy()
    option_spec.update({
        'abstractmethod': directives.flag,
        'classmethod': directives.flag,
        'type': directives.unchanged,
    })

    def handle_signature(self, sig: str, signode: desc_signature) -> tuple[str, str]:
        fullname, prefix = super().handle_signature(sig, signode)

        typ = self.options.get('type')
        if typ:
            annotations = _parse_annotation(typ, self.env)
            signode += addnodes.desc_annotation(typ, '',
                                                addnodes.desc_sig_punctuation('', ':'),
                                                addnodes.desc_sig_space(),
                                                *annotations)

        return fullname, prefix

    def get_signature_prefix(self, sig: str) -> list[nodes.Node]:
        prefix: list[nodes.Node] = []
        if 'abstractmethod' in self.options:
            prefix.append(nodes.Text('abstract'))
            prefix.append(addnodes.desc_sig_space())
        if 'classmethod' in self.options:
            prefix.append(nodes.Text('class'))
            prefix.append(addnodes.desc_sig_space())

        prefix.append(nodes.Text('property'))
        prefix.append(addnodes.desc_sig_space())
        return prefix

    def get_index_text(self, modname: str, name_cls: tuple[str, str]) -> str:
        name, cls = name_cls
        try:
            clsname, attrname = name.rsplit('.', 1)
            if modname and self.env.config.add_module_names:
                clsname = '.'.join([modname, clsname])
        except ValueError:
            if modname:
                return _('%s (in module %s)') % (name, modname)
            else:
                return name

        return _('%s (%s property)') % (attrname, clsname)


class PyModule(SphinxDirective):
    """
    Directive to mark description of a new module.
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec: OptionSpec = {
        'platform': lambda x: x,
        'synopsis': lambda x: x,
        'noindex': directives.flag,
        'nocontentsentry': directives.flag,
        'deprecated': directives.flag,
    }

    def run(self) -> list[Node]:
        domain = cast(GAUSSDomain, self.env.get_domain('gauss'))

        modname = self.arguments[0].strip()
        noindex = 'noindex' in self.options
        self.env.ref_context['gauss:module'] = modname

        content_node: Element = nodes.section()
        # necessary so that the child nodes get the right source/line set
        content_node.document = self.state.document
        nested_parse_with_titles(self.state, self.content, content_node, self.content_offset)

        ret: list[Node] = []
        if not noindex:
            # note module to the domain
            node_id = make_id(self.env, self.state.document, 'module', modname)
            target = nodes.target('', '', ids=[node_id], ismod=True)
            self.set_source_info(target)
            self.state.document.note_explicit_target(target)

            domain.note_module(modname,
                               node_id,
                               self.options.get('synopsis', ''),
                               self.options.get('platform', ''),
                               'deprecated' in self.options)
            domain.note_object(modname, 'module', node_id, location=target)

            # the platform and synopsis aren't printed; in fact, they are only
            # used in the modindex currently
            ret.append(target)
            indextext = f'module; {modname}'
            inode = addnodes.index(entries=[('pair', indextext, node_id, '', None)])
            ret.append(inode)
        ret.extend(content_node.children)
        return ret


class PyCurrentModule(SphinxDirective):
    """
    This directive is just to tell Sphinx that we're documenting
    stuff in module foo, but links to module foo won't lead here.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec: OptionSpec = {}

    def run(self) -> list[Node]:
        modname = self.arguments[0].strip()
        if modname == 'None':
            self.env.ref_context.pop('gauss:module', None)
        else:
            self.env.ref_context['gauss:module'] = modname
        return []


class PyXRefRole(XRefRole):
    def process_link(self, env: BuildEnvironment, refnode: Element,
                     has_explicit_title: bool, title: str, target: str) -> tuple[str, str]:
        refnode['gauss:module'] = env.ref_context.get('gauss:module')
        refnode['gauss:class'] = env.ref_context.get('gauss:class')
        if not has_explicit_title:
            title = title.lstrip('.')    # only has a meaning for the target
            target = target.lstrip('~')  # only has a meaning for the title
            # if the first character is a tilde, don't display the module/class
            # parts of the contents
            if title[0:1] == '~':
                title = title[1:]
                dot = title.rfind('.')
                if dot != -1:
                    title = title[dot + 1:]
        # if the first character is a dot, search more specific namespaces first
        # else search builtins first
        if target[0:1] == '.':
            target = target[1:]
            refnode['refspecific'] = True
        return title, target


def filter_meta_fields(app: Sphinx, domain: str, objtype: str, content: Element) -> None:
    """Filter ``:meta:`` field from its docstring."""
    if domain != 'gauss':
        return

    for node in content:
        if isinstance(node, nodes.field_list):
            fields = cast(List[nodes.field], node)
            # removing list items while iterating the list needs reversed()
            for field in reversed(fields):
                field_name = cast(nodes.field_body, field[0]).astext().strip()
                if field_name == 'meta' or field_name.startswith('meta '):
                    node.remove(field)


class PythonModuleIndex(Index):
    """
    Index subclass to provide the Python module index.
    """

    name = 'modindex'
    localname = _('GAUSS Module Index')
    shortname = _('modules')

    def generate(self, docnames: Iterable[str] | None = None,
                 ) -> tuple[list[tuple[str, list[IndexEntry]]], bool]:
        content: dict[str, list[IndexEntry]] = {}
        # list of prefixes to ignore
        ignores: list[str] = self.domain.env.config['modindex_common_prefix']
        ignores = sorted(ignores, key=len, reverse=True)
        # list of all modules, sorted by module name
        modules = sorted(self.domain.data['modules'].items(),
                         key=lambda x: x[0].lower())
        # sort out collapsible modules
        prev_modname = ''
        num_toplevels = 0
        for modname, (docname, node_id, synopsis, platforms, deprecated) in modules:
            if docnames and docname not in docnames:
                continue

            for ignore in ignores:
                if modname.startswith(ignore):
                    modname = modname[len(ignore):]
                    stripped = ignore
                    break
            else:
                stripped = ''

            # we stripped the whole module name?
            if not modname:
                modname, stripped = stripped, ''

            entries = content.setdefault(modname[0].lower(), [])

            package = modname.split('.')[0]
            if package != modname:
                # it's a submodule
                if prev_modname == package:
                    # first submodule - make parent a group head
                    if entries:
                        last = entries[-1]
                        entries[-1] = IndexEntry(last[0], 1, last[2], last[3],
                                                 last[4], last[5], last[6])
                elif not prev_modname.startswith(package):
                    # submodule without parent in list, add dummy entry
                    entries.append(IndexEntry(stripped + package, 1, '', '', '', '', ''))
                subtype = 2
            else:
                num_toplevels += 1
                subtype = 0

            qualifier = _('Deprecated') if deprecated else ''
            entries.append(IndexEntry(stripped + modname, subtype, docname,
                                      node_id, platforms, qualifier, synopsis))
            prev_modname = modname

        # apply heuristics when to collapse modindex at page load:
        # only collapse if number of toplevel modules is larger than
        # number of submodules
        collapse = len(modules) - num_toplevels < num_toplevels

        # sort by first letter
        sorted_content = sorted(content.items())

        return sorted_content, collapse


class GAUSSDomain(Domain):
    """GAUSS language domain."""
    name = 'gauss'
    label = 'GAUSS'
    object_types: dict[str, ObjType] = {
        'function':     ObjType(_('function'),      'func', 'obj'),
        'data':         ObjType(_('data'),          'data', 'obj'),
        'class':        ObjType(_('class'),         'class', 'exc', 'obj'),
        'exception':    ObjType(_('exception'),     'exc', 'class', 'obj'),
        'method':       ObjType(_('method'),        'meth', 'obj'),
        'classmethod':  ObjType(_('class method'),  'meth', 'obj'),
        'staticmethod': ObjType(_('static method'), 'meth', 'obj'),
        'attribute':    ObjType(_('attribute'),     'attr', 'obj'),
        'property':     ObjType(_('property'),      'attr', '_prop', 'obj'),
        'module':       ObjType(_('module'),        'mod', 'obj'),
    }

    directives = {
        'function':        PyFunction,
        'data':            PyVariable,
        'class':           PyClasslike,
        'exception':       PyClasslike,
        'method':          PyMethod,
        'classmethod':     PyClassMethod,
        'staticmethod':    PyStaticMethod,
        'attribute':       PyAttribute,
        'property':        PyProperty,
        'module':          PyModule,
        'currentmodule':   PyCurrentModule,
        'decorator':       PyDecoratorFunction,
        'decoratormethod': PyDecoratorMethod,
    }
    roles = {
        'data':  PyXRefRole(),
        'exc':   PyXRefRole(),
        'func':  PyXRefRole(fix_parens=True),
        'class': PyXRefRole(),
        'const': PyXRefRole(),
        'attr':  PyXRefRole(),
        'meth':  PyXRefRole(fix_parens=True),
        'mod':   PyXRefRole(),
        'obj':   PyXRefRole(),
    }
    initial_data: dict[str, dict[str, tuple[Any]]] = {
        'objects': {},  # fullname -> docname, objtype
        'modules': {},  # modname -> docname, synopsis, platform, deprecated
    }
    indices = [
        PythonModuleIndex,
    ]

    @property
    def objects(self) -> dict[str, ObjectEntry]:
        return self.data.setdefault('objects', {})  # fullname -> ObjectEntry

    def note_object(self, name: str, objtype: str, node_id: str,
                    aliased: bool = False, location: Any = None) -> None:
        """Note a python object for cross reference.

        .. versionadded:: 2.1
        """
        if name in self.objects:
            other = self.objects[name]
            if other.aliased and aliased is False:
                # The original definition found. Override it!
                pass
            elif other.aliased is False and aliased:
                # The original definition is already registered.
                return
            else:
                # duplicated
                logger.warning(__('duplicate object description of %s, '
                                  'other instance in %s, use :noindex: for one of them'),
                               name, other.docname, location=location)
        self.objects[name] = ObjectEntry(self.env.docname, node_id, objtype, aliased)


    @property
    def modules(self) -> dict[str, ModuleEntry]:
        return self.data.setdefault('modules', {})  # modname -> ModuleEntry

    def note_module(self, name: str, node_id: str, synopsis: str,
                    platform: str, deprecated: bool) -> None:
        """Note a python module for cross reference.

        .. versionadded:: 2.1
        """
        self.modules[name] = ModuleEntry(self.env.docname, node_id,
                                         synopsis, platform, deprecated)

    def clear_doc(self, docname: str) -> None:
        for fullname, obj in list(self.objects.items()):
            if obj.docname == docname:
                del self.objects[fullname]
        for modname, mod in list(self.modules.items()):
            if mod.docname == docname:
                del self.modules[modname]

    def merge_domaindata(self, docnames: list[str], otherdata: dict[str, Any]) -> None:
        # XXX check duplicates?
        for fullname, obj in otherdata['objects'].items():
            if obj.docname in docnames:
                self.objects[fullname] = obj
        for modname, mod in otherdata['modules'].items():
            if mod.docname in docnames:
                self.modules[modname] = mod

    def _search_objects(self, name, objtypes=None):
        newname = None
        newobj = None

        for k in self.objects:
            if name.casefold() == k.casefold():
                if not objtypes or self.objects[k][1] in objtypes:
                    newname = k
                    newobj = self.objects[k]

                break

        return (newname, newobj, )

    def find_obj(self, env: BuildEnvironment, modname: str, classname: str,
                 name: str, type: str | None, searchmode: int = 0,
                 ) -> list[tuple[str, ObjectEntry]]:
        # type: (BuildEnvironment, unicode, unicode, unicode, unicode, int) -> List[Tuple[unicode, Any]]  # NOQA
        """Find a Python object for "name", perhaps using the given module
        and/or classname.  Returns a list of (name, object entry) tuples.
        """
        # skip parens
        if name[-2:] == '()':
            name = name[:-2]

        if not name:
            return []

        matches = []  # type: List[Tuple[unicode, Any]]

        newname = None
        newobj = None
        if searchmode == 1:
            if type is None:
                objtypes = list(self.object_types)
            else:
                objtypes = self.objtypes_for_role(type)
            if objtypes is not None:
                if modname and classname:
                    newname, newobj = self._search_objects(modname + '.' + classname + '.' + name, objtypes)

                if not newname and modname:
                    newname, newobj = self._search_objects(modname + '.' + name, objtypes)

                if not newname:
                    newname, newobj = self._search_objects(name, objtypes)

                if not newname:
                    # "fuzzy" searching mode
                    searchname = ('.' + name).casefold()
                    matches = [(oname, self.objects[oname]) for oname in self.objects
                               if oname.casefold().endswith(searchname) and
                               self.objects[oname][1] in objtypes]
        else:
            # NOTE: searching for exact match, object type is not considered

            newname, newobj = self._search_objects(name)

            #if name in objects:
            #    newname = name
            if not newname and type == 'mod':
                # only exact matches allowed for modules
                return []

            if not newname and classname:
                newname, newobj = self._search_objects(classname + '.' + name)
            
            if not newname and modname:
                newname, newobj = self._search_objects(modname + '.' + name)

            if not newname and modname and classname:
                newname, newobj = self._search_objects(modname + '.' + classname + '.' + name)

            if not newname and type == 'exc' and '.' not in name:
                # special case: builtin exceptions have module "exceptions" set
                newname, newobj = self._search_objects('exceptions.' + name)

            if not newname and type in ('func', 'meth') and '.' not in name:
                # special case: object methods
                newname, newobj = self._search_objects('object.' + name)

        if newname is not None:
            matches.append((newname, newobj))
        return matches

    def resolve_xref(self, env: BuildEnvironment, fromdocname: str, builder: Builder,
                     type: str, target: str, node: pending_xref, contnode: Element,
                     ) -> Element | None:
        modname = node.get('gauss:module')
        clsname = node.get('gauss:class')
        searchmode = 1 if node.hasattr('refspecific') else 0
        matches = self.find_obj(env, modname, clsname, target,
                                type, searchmode)

        if not matches and type == 'attr':
            # fallback to meth (for property; Sphinx 2.4.x)
            # this ensures that `:attr:` role continues to refer to the old property entry
            # that defined by ``method`` directive in old reST files.
            matches = self.find_obj(env, modname, clsname, target, 'meth', searchmode)
        if not matches and type == 'meth':
            # fallback to attr (for property)
            # this ensures that `:meth:` in the old reST files can refer to the property
            # entry that defined by ``property`` directive.
            #
            # Note: _prop is a secret role only for internal look-up.
            matches = self.find_obj(env, modname, clsname, target, '_prop', searchmode)

        if not matches:
            return None
        elif len(matches) > 1:
            canonicals = [m for m in matches if not m[1].aliased]
            if len(canonicals) == 1:
                matches = canonicals
            else:
                logger.warning(__('more than one target found for cross-reference %r: %s'),
                               target, ', '.join(match[0] for match in matches),
                               type='ref', subtype='python', location=node)
        name, obj = matches[0]

        if obj[2] == 'module':
            return self._make_module_refnode(builder, fromdocname, name, contnode)
        else:
            # determine the content of the reference by conditions
            content = find_pending_xref_condition(node, 'resolved')
            if content:
                children = content.children
            else:
                # if not found, use contnode
                children = [contnode]

            return make_refnode(builder, fromdocname, obj[0], obj[1], children, name)

    def resolve_any_xref(self, env: BuildEnvironment, fromdocname: str, builder: Builder,
                         target: str, node: pending_xref, contnode: Element,
                         ) -> list[tuple[str, Element]]:
        modname = node.get('gauss:module')
        clsname = node.get('gauss:class')
        results: list[tuple[str, Element]] = []

        # always search in "refspecific" mode with the :any: role
        matches = self.find_obj(env, modname, clsname, target, None, 1)
        multiple_matches = len(matches) > 1

        for name, obj in matches:

            if multiple_matches and obj.aliased:
                # Skip duplicated matches
                continue

            if obj[2] == 'module':
                results.append(('gauss:mod',
                                self._make_module_refnode(builder, fromdocname,
                                                          name, contnode)))
            else:
                # determine the content of the reference by conditions
                content = find_pending_xref_condition(node, 'resolved')
                if content:
                    children = content.children
                else:
                    # if not found, use contnode
                    children = [contnode]

                results.append(('gauss:' + self.role_for_objtype(obj[2]),
                                make_refnode(builder, fromdocname, obj[0], obj[1],
                                             children, name)))
        return results

    def _make_module_refnode(self, builder: Builder, fromdocname: str, name: str,
                             contnode: Node) -> Element:
        # get additional info for modules
        module = self.modules[name]
        title = name
        if module.synopsis:
            title += ': ' + module.synopsis
        if module.deprecated:
            title += _(' (deprecated)')
        if module.platform:
            title += ' (' + module.platform + ')'
        return make_refnode(builder, fromdocname, module.docname, module.node_id,
                            contnode, title)

    def get_objects(self) -> Iterator[tuple[str, str, str, str, str, int]]:
        for modname, mod in self.modules.items():
            yield (modname, modname, 'module', mod.docname, mod.node_id, 0)
        for refname, obj in self.objects.items():
            if obj.objtype != 'module':  # modules are already handled
                if obj.aliased:
                    # aliased names are not full-text searchable.
                    yield (refname, refname, obj.objtype, obj.docname, obj.node_id, -1)
                else:
                    yield (refname, refname, obj.objtype, obj.docname, obj.node_id, 1)

    def get_full_qualified_name(self, node: Element) -> str | None:
        modname = node.get('gauss:module')
        clsname = node.get('gauss:class')
        target = node.get('reftarget')
        if target is None:
            return None
        else:
            return '.'.join(filter(None, [modname, clsname, target]))

def builtin_resolver(app: Sphinx, env: BuildEnvironment,
                     node: pending_xref, contnode: Element) -> Element | None:
    """Do not emit nitpicky warnings for built-in types."""
    def istyping(s: str) -> bool:
        if s.startswith('typing.'):
            s = s.split('.', 1)[1]

        return s in typing.__all__

    if node.get('refdomain') != 'gauss':
        return None
    elif node.get('reftype') in ('class', 'obj') and node.get('reftarget') == 'None':
        return contnode
    elif node.get('reftype') in ('class', 'obj', 'exc'):
        reftarget = node.get('reftarget')
        if inspect.isclass(getattr(builtins, reftarget, None)):
            # built-in class
            return contnode
        if istyping(reftarget):
            # typing class
            return contnode

    return None

def setup(app: Sphinx) -> dict[str, Any]:
    app.setup_extension('sphinx.directives')

    app.add_domain(GAUSSDomain)
    app.add_node(desc_returnlist)
    app.add_node(desc_return)

    #app.add_config_value('python_use_unqualified_type_names', False, 'env')
    #app.add_config_value('python_maximum_signature_line_length', None, 'env',
    #                     types={int, None})
    #app.add_config_value('python_display_short_literal_types', False, 'env')
    #app.connect('object-description-transform', filter_meta_fields)
    app.connect('missing-reference', builtin_resolver, priority=900)

    return {
        'version': 'builtin',
        'env_version': 4,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
