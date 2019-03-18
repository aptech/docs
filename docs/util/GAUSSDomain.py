"""
    sphinx.domains.gauss
    ~~~~~~~~~~~~~~~~

    The GAUSS language domain. Based on the GAUSS language domain.

    :copyright: Copyright 2007-2019 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
import string

from docutils import nodes

from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, ObjType
from sphinx.locale import _
from sphinx.roles import XRefRole
from sphinx.util.docfields import Field, TypedField
from sphinx.util.nodes import make_refnode

if False:
    # For type annotation
    from typing import Any, Dict, Iterator, List, Tuple  # NOQA
    from sphinx.application import Sphinx  # NOQA
    from sphinx.builders import Builder  # NOQA
    from sphinx.environment import BuildEnvironment  # NOQA


# RE to split at word boundaries
wsplit_re = re.compile(r'(\W+)')
id_re = re.compile(r'([a-zA-Z_]\w*)')

# REs for GAUSS signatures
gauss_function_re = re.compile(
    r'''(?:\(?\s*(\d+)\s*\)?)?(?:\s*=)?\s*   # of return args
        (.*?)\s*                             # function name
        (?:\(\s*(.*?)\s*\))?$       # function args
    ''', re.VERBOSE)

#gauss_proc_re = re.compile(
#    r'''\bproc\b\s*(?:\(?\s*(?<procreturns>\d+)\s*\)?)?(?:\s*=)?\s*(?<procname>%1)\s*(?:\(\s*(?<procargs>%2)\s*\))?\s*;
#    ''', re.VERBOSE)
#
#gauss_keyword_re = re.compile(
#    r'''\bkeyword\b\s+(?<kwname>%1)\s*\((?<kwargs>%2)\)\s*;
#    ''', re.VERBOSE)
#
#gauss_fn_re = re.compile(
#    r'''\bfn\b\s+(?<fnname>%1)\s*(?:\((?<fnargs>%2)\)\s*)?\=
#    ''', re.VERBOSE)

gauss_sig_re = re.compile(
    r'''^([^(]*?)          # return type
        ([\w:.]+)  \s*     # thing name (colon allowed for C++)
        (?: \((.*)\) )?    # optionally arguments
        (\s+const)? $      # const specifier
    ''', re.VERBOSE)
gauss_funcptr_sig_re = re.compile(
    r'''^([^(]+?)          # return type
        (\( [^()]+ \)) \s* # name in parentheses
        \( (.*) \)         # arguments
        (\s+const)? $      # const specifier
    ''', re.VERBOSE)
gauss_funcptr_arg_sig_re = re.compile(
    r'''^\s*([^(,]+?)      # return type
        \( ([^()]+) \) \s* # name in parentheses
        \( (.*) \)         # arguments
        (\s+const)?        # const specifier
        \s*(?=$|,)         # end with comma or end of string
    ''', re.VERBOSE)
gauss_funcptr_name_re = re.compile(r'^\(\s*\*\s*(.*?)\s*\)$')


class GAUSSObject(ObjectDescription):
    """
    Description of a GAUSS language object.
    """

    doc_field_types = [
        TypedField('parameter', label=_('Parameters'),
                   names=('param', 'parameter', 'arg', 'argument'),
                   typerolename='type', typenames=('type',)),
        Field('returnvalue', label=_('Returns'), has_arg=False,
              names=('returns', 'return')),
        Field('returntype', label=_('Return type'), has_arg=False,
              names=('rtype',)),
    ]

    # These GAUSS types aren't described anywhere, so don't try to create
    # a cross-reference to them
    stopwords = set(("and", "bool", "break", "call", "callexe", "checkinterrupt", "clear", "clearg", "closeall", "cls", "comlog", "compile",
               "continue", "create", "debug", "declare", "delete", "disable", "dlibrary", "dllcall", "do", "dos", "edit", "ed", "else",
               "elseif", "enable", "end", "endfor", "endif", "endp", "endo", "errorlog", "errorlogat", "expr", "external", "fn",
               "format", "for", "goto", "gosub", "graph", "if", "keyword", "library", "library", "line", "load", "loadarray", "loadexe",
               "loadf", "loadk", "loadm", "loadp", "loads", "loadx", "locate", "loopnextindex", "lprint", "lpwidth", "lshow",
               "msym", "ndpclex", "new", "not", "open", "or", "output", "outwidth", "plotsym", "plot", "pop", "prcsn", "print",
               "printdos", "proc", "push", "retp", "return", "rndcon", "rndmod", "rndmult", "rndseed", "run", "saveall", "save", "screen",
               "scroll", "setarray", "show", "stop", "system", "trace", "trap", "threadfor", "threadendfor", "threadbegin", "threadjoin",
               "threadstat", "threadend", "until", "use", "while", "winprint", "with"))

    def _parse_type(self, node, ctype):
        # type: (nodes.Element, str) -> None
        # add cross-ref nodes for all words
        for part in [_f for _f in wsplit_re.split(ctype) if _f]:
            tnode = nodes.Text(part, part)
            if part[0] in string.ascii_letters + '_' and \
               part not in self.stopwords:
                pnode = addnodes.pending_xref(
                    '', refdomain='gauss', reftype='type', reftarget=part,
                    modname=None, classname=None)
                pnode += tnode
                node += pnode
            else:
                node += tnode

    def _parse_arglist(self, arglist):
        # type: (str) -> Iterator[str]
        while True:
            m = gauss_funcptr_arg_sig_re.match(arglist)
            if m:
                yield m.group()
                arglist = gauss_funcptr_arg_sig_re.sub('', arglist)
                if ',' in arglist:
                    _, arglist = arglist.split(',', 1)
                else:
                    break
            else:
                if ',' in arglist:
                    arg, arglist = arglist.split(',', 1)
                    yield arg
                else:
                    yield arglist
                    break

    def handle_signature(self, sig, signode):
        # type: (str, addnodes.desc_signature) -> str
        """Transform a GAUSS signature into RST nodes."""
        # first try the function pointer signature regex, it's more specific
        m = gauss_function_re.match(sig)
        #m = gauss_funcptr_sig_re.match(sig)
        #if m is None:
        #    m = gauss_sig_re.match(sig)
        if m is None:
            raise ValueError('no match')
        functype, numrets, name, arglist = m.groups()

        print("name = {}".format(name))

        desc_type = addnodes.desc_type('', '')
        signode += desc_type
        self._parse_type(desc_type, functype)
        try:
            classname, funcname = name.split('::', 1)
            classname += '::'
            signode += addnodes.desc_addname(classname, classname)
            signode += addnodes.desc_name(funcname, funcname)
            # name (the full name) is still both parts
        except ValueError:
            signode += addnodes.desc_name(name, name)
        # clean up parentheses from canonical name
        #m = gauss_funcptr_name_re.match(name)
        #if m:
        #    name = m.group(1)

        typename = self.env.ref_context.get('gauss:type')
        if self.name == 'gauss:member' and typename:
            fullname = typename + '.' + name
        else:
            fullname = name

        if not arglist:
            if self.objtype == 'function' or \
                    self.objtype == 'macro' and sig.rstrip().endswith('()'):
                # for functions, add an empty parameter list
                signode += addnodes.desc_parameterlist()
            #if const:
            #    signode += addnodes.desc_addname(const, const)
            return fullname

        paramlist = addnodes.desc_parameterlist()
        arglist = arglist.replace('`', '').replace('\\ ', '')  # remove markup
        # this messes up function pointer types, but not too badly ;)
        for arg in self._parse_arglist(arglist):
            arg = arg.strip()
            param = addnodes.desc_parameter('', '', noemph=True)
            try:
                m = gauss_funcptr_arg_sig_re.match(arg)
                if m:
                    self._parse_type(param, m.group(1) + '(')
                    param += nodes.emphasis(m.group(2), m.group(2))
                    self._parse_type(param, ')(' + m.group(3) + ')')
                    if m.group(4):
                        param += addnodes.desc_addname(m.group(4), m.group(4))
                else:
                    ctype, argname = arg.rsplit(' ', 1)
                    self._parse_type(param, ctype)
                    # separate by non-breaking space in the output
                    param += nodes.emphasis(' ' + argname, '\xa0' + argname)
            except ValueError:
                # no argument name given, only the type
                self._parse_type(param, arg)
            paramlist += param
        signode += paramlist
        #if const:
        #    signode += addnodes.desc_addname(const, const)
        return fullname

    def get_index_text(self, name):
        # type: (str) -> str
        if self.objtype == 'function':
            return _('%s (GAUSS function)') % name
        elif self.objtype == 'member':
            return _('%s (GAUSS member)') % name
        elif self.objtype == 'macro':
            return _('%s (GAUSS macro)') % name
        elif self.objtype == 'type':
            return _('%s (GAUSS type)') % name
        elif self.objtype == 'var':
            return _('%s (GAUSS variable)') % name
        else:
            return ''

    def add_target_and_index(self, name, sig, signode):
        # type: (str, str, addnodes.desc_signature) -> None
        # for GAUSS API items we add a prefix since names are usually not qualified
        # by a module name and so easily clash with e.g. section titles
        targetname = 'gauss.' + name
        if targetname not in self.state.document.ids:
            signode['names'].append(targetname)
            signode['ids'].append(targetname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            inv = self.env.domaindata['gauss']['objects']
            if name in inv:
                self.state_machine.reporter.warning(
                    'duplicate GAUSS object description of %s, ' % name +
                    'other instance in ' + self.env.doc2path(inv[name][0]),
                    line=self.lineno)
            inv[name] = (self.env.docname, self.objtype)

        indextext = self.get_index_text(name)
        if indextext:
            self.indexnode['entries'].append(('single', indextext,
                                              targetname, '', None))

    def before_content(self):
        # type: () -> None
        self.typename_set = False
        if self.name == 'gauss:type':
            if self.names:
                self.env.ref_context['gauss:type'] = self.names[0]
                self.typename_set = True

    def after_content(self):
        # type: () -> None
        if self.typename_set:
            self.env.ref_context.pop('gauss:type', None)


class GAUSSXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        # type: (BuildEnvironment, nodes.Element, bool, str, str) -> Tuple[str, str]
        if not has_explicit_title:
            target = target.lstrip('~')  # only has a meaning for the title
            # if the first character is a tilde, don't display the module/class
            # parts of the contents
            if title[0:1] == '~':
                title = title[1:]
                dot = title.rfind('.')
                if dot != -1:
                    title = title[dot + 1:]
        return title, target


class GAUSSDomain(Domain):
    """GAUSS language domain."""
    name = 'gauss'
    label = 'GAUSS'
    object_types = {
        'function': ObjType(_('function'), 'func'),
        'member':   ObjType(_('member'),   'member'),
        'macro':    ObjType(_('macro'),    'macro'),
        'type':     ObjType(_('type'),     'type'),
        'var':      ObjType(_('variable'), 'data'),
    }

    directives = {
        'function': GAUSSObject,
        'member':   GAUSSObject,
        'macro':    GAUSSObject,
        'type':     GAUSSObject,
        'var':      GAUSSObject,
    }
    roles = {
        'func':   GAUSSXRefRole(fix_parens=True),
        'member': GAUSSXRefRole(),
        'macro':  GAUSSXRefRole(),
        'data':   GAUSSXRefRole(),
        'type':   GAUSSXRefRole(),
    }
    initial_data = {
        'objects': {},  # fullname -> docname, objtype
    }  # type: Dict[str, Dict[str, Tuple[str, Any]]]

    def clear_doc(self, docname):
        # type: (str) -> None
        for fullname, (fn, _l) in list(self.data['objects'].items()):
            if fn == docname:
                del self.data['objects'][fullname]

    def merge_domaindata(self, docnames, otherdata):
        # type: (List[str], Dict) -> None
        # XXX check duplicates
        for fullname, (fn, objtype) in otherdata['objects'].items():
            if fn in docnames:
                self.data['objects'][fullname] = (fn, objtype)

    def resolve_xref(self, env, fromdocname, builder,
                     typ, target, node, contnode):
        # type: (BuildEnvironment, str, Builder, str, str, addnodes.pending_xref, nodes.Element) -> nodes.Element  # NOQA
        # strip pointer asterisk
        target = target.rstrip(' *')
        # becase TypedField can generate xrefs
        if target in GAUSSObject.stopwords:
            return contnode
        if target not in self.data['objects']:
            return None
        obj = self.data['objects'][target]
        return make_refnode(builder, fromdocname, obj[0], 'gauss.' + target,
                            contnode, target)

    def resolve_any_xref(self, env, fromdocname, builder, target,
                         node, contnode):
        # type: (BuildEnvironment, str, Builder, str, addnodes.pending_xref, nodes.Element) -> List[Tuple[str, nodes.Element]]  # NOQA
        # strip pointer asterisk
        target = target.rstrip(' *')
        if target not in self.data['objects']:
            return []
        obj = self.data['objects'][target]
        return [('gauss:' + self.role_for_objtype(obj[1]),
                 make_refnode(builder, fromdocname, obj[0], 'gauss.' + target,
                              contnode, target))]

    def get_objects(self):
        # type: () -> Iterator[Tuple[str, str, str, str, str, int]]
        for refname, (docname, type) in list(self.data['objects'].items()):
            yield (refname, refname, type, docname, 'gauss.' + refname, 1)


#def setup(app):
#    # type: (Sphinx) -> Dict[str, Any]
#    app.add_domain(GAUSSDomain)
#
#    return {
#        'version': 'builtin',
#        'env_version': 1,
#        'parallel_read_safe': True,
#        'parallel_write_safe': True,
#    }
