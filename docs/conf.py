# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'GAUSS'
copyright = '2024, Aptech Systems, Inc'
author = 'Aptech Systems, Inc'

# The short X.Y version
version = '24'
# The full version, including alpha/beta/rc tags
release = '24'


# -- General configuration ---------------------------------------------------

primary_domain = 'gauss'

default_role = 'any'

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_design',
    'sphinx_tabs.tabs',
]

mathjax3_config = {
    'extensions': ['tex2jax.js'],
    'jax': ['input/TeX', 'output/HTML-CSS'],
    'HTML-CSS': { 'fonts': ['TeX'] }
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
#language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['dbnomics_datasets*.rst', 'dbnomics_series_*.rst', 'dbnomics_last_updates.rst', 'dbnomics_list_providers.rst', 'dbnomics_provider.rst', 
                    'fred_category*.rst', 'fred_release*.rst', 'fred_series*.rst', 'fred_tags*.rst', 'fred_source*.rst', 'fred_related*.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

highlight_language = 'gauss'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
#html_theme_path = ["_themes"]
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates', '_themes/pydata_sphinx_theme/static']
templates_path = ['_templates']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.7.1/css/fontawesome.min.css',
        'https://fonts.googleapis.com/css?family=Lato',
        '_static/theme_override.css',
        '_static/design-style.59c74d8c95b765a7fd995ac71d459ebe.min.css',
        '_static/tabs.css',
        '_static/pygments-custom.css',
        '_static/sphinx_design.min.css',
    ],
    'default_mode': 'light'
}

html_js_files = [
    'https://www.googletagmanager.com/gtag/js?id=G-WLDRLMK7MW',
    'ga.js',
    'https://js.hs-scripts.com/4366389.js'
]

html_logo = '_static/images/aptech-logo.png'

html_theme_options = {
    'navbar_end': ['navbar-icon-links'],
    'article_header_start': None
}

#html_theme_options = {
#    'prev_next_buttons_location': 'both',
#    'style_external_links': True,
#    'style_nav_header_background': '#fff',
#    'logo_only': True,
#    'canonical_url': 'https://docs.aptech.com/gauss/'
#}

html_baseurl = 'https://docs.aptech.com/gauss/'

html_short_title = '{} {} documentation'.format(project, version)
html_title = html_short_title + ' | Aptech'

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'GAUSSdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'GAUSS.tex', 'GAUSS Documentation',
     'Aptech', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'gauss', 'GAUSS Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'GAUSS', 'GAUSS Documentation',
     author, 'GAUSS', 'The GAUSS Platform',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------

def setup(sphinx):
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'util')))

    from GAUSSLexer import GAUSSLexer
    sphinx.add_lexer("gauss", GAUSSLexer)

    import GAUSSDomain
    GAUSSDomain.setup(sphinx)

    import GAUSSRoles
    GAUSSRoles.setup(sphinx)

    from GAUSSHTMLTranslator import GAUSSHTMLTranslator

    builders = ['html', 'readthedocs', 'readthedocssinglehtmllocalmedia']

    def on_builder_inited(app):
        if app.builder.name in builders:
            app.set_translator(app.builder.name, GAUSSHTMLTranslator, override=True)

    # Connect the on_builder_inited function to the 'builder-inited' event
    sphinx.connect('builder-inited', on_builder_inited)

    #for builder in ['html', 'readthedocs', 'readthedocssinglehtmllocalmedia']:
    #    sphinx.set_translator(builder,
    #                          GAUSSHTMLTranslator,
    #                          override=True)

