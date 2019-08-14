from sphinx import addnodes
import GAUSSDomain
from sphinx.writers.html import HTMLTranslator


class GAUSSHTMLTranslator(HTMLTranslator):
    """
    Our custom GAUSS HTML translator.
    """

    def unknown_visit(self, node):
        super().unknown_visit(node)

    def __init__(self, *args):
        super().__init__(*args)
        self.return_count = 0

    # def visit_desc_name(self, node):
    #     # type: (nodes.Element) -> None
    #     self.body.append(self.starttag(node, 'code', '', CLASS='descname'))
    #
    # def depart_desc_name(self, node):
    #     # type: (nodes.Element) -> None
    #     self.body.append('</code>')

    def visit_desc_returnlist(self, node):
        # type: (nodes.Element) -> None

        self.return_count = sum(
            [isinstance(c, GAUSSDomain.desc_return) # source.docs.util.
             for c in node.children])
        # How many required parameters are left.
        self.required_params_left = self.return_count

        if self.return_count > 1:
            self.body.append('<span class="sig-curly">{</span> ')

        self.param_separator = node.child_text_separator

    def depart_desc_returnlist(self, node):
        # type: (nodes.Element) -> None
        if self.return_count > 1:
            self.body.append(' <span class="sig-curly">}</span>')

        self.body.append(' <span class="sig-equals">=</span> ')

    # If required parameters are still to come, then put the comma after
    # the parameter.  Otherwise, put the comma before.  This ensures that
    # signatures like the following render correctly (see issue #1001):
    #
    #     foo([a, ]b, c[, d])
    #
    def visit_desc_return(self, node):
        # type: (nodes.Element) -> None
        if not self.required_params_left:
            self.body.append(self.param_separator)
        self.required_params_left -= 1
        if not node.hasattr('noemph'):
            self.body.append('<em>')

    def depart_desc_return(self, node):
        # type: (nodes.Element) -> None
        if not node.hasattr('noemph'):
            self.body.append('</em>')
        if self.required_params_left:
            self.body.append(self.param_separator)
