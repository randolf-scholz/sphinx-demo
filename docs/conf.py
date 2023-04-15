r"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup -------------------------------------------------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import datetime
import os
import sys
from importlib import metadata

os.environ["GENERATING_DOCS"] = "true"
sys.path.insert(0, os.path.abspath("."))
sys.path.append(os.path.abspath("./_ext"))

AUTHOR = "Randolf Scholz"
MODULE = "sphinx_demo"
MODULE_DIR = "src/sphinx_demo"
VERSION = metadata.version(MODULE)
YEAR = datetime.datetime.now().year


# region Project Information ------------------------------------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sphinx-demo"
# The documented project’s name.

author = "Randolf Scholz"
# The author name(s) of the document. The default value is 'unknown'.

project_copyright = f"{YEAR}, {AUTHOR}"
# A copyright statement in the style '2008, Author Name'.

version = VERSION
# The major project version, used as the replacement for |version|.
# For example, for the Python documentation, this may be something like 2.6.

release = version
# The full project version, used as the replacement for |release| and e.g. in the HTML templates.
# For example, for the Python documentation, this may be something like 2.6.0rc1.

# endregion Project Information ---------------------------------------------------------------------------------------


# region General Configuration ----------------------------------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # "sphinx_toolbox.more_autodoc.typehints",
    # "sphinx_toolbox.more_autodoc.typevars",
    # "sphinx_toolbox.more_autodoc.genericalias",
    # Sphinx builtin extensions
    # "sphinx.ext.autodoc",
    # "sphinx.ext.autosectionlabel",
    # "sphinx.ext.autosummary",
    # "sphinx.ext.coverage",
    # "sphinx.ext.doctest",
    # "sphinx.ext.duration",
    # "sphinx.ext.intersphinx",
    # "sphinx.ext.mathjax",
    # "sphinx.ext.napoleon",
    # "sphinx.ext.todo",
    # "sphinx.ext.viewcode",
    # # 1st party extensions
    # "signatures",
    # # 3rd party extensions
    "autoapi.extension",
    # "sphinx_copybutton",
    "sphinx_math_dollar",
    # "sphinx_autodoc_typehints",
]
# Add any Sphinx extension module names here, as strings. They can be extensions coming with Sphinx
# (named 'sphinx.ext.*') or your custom ones.


root_doc = "index"
# The document name of the “root” document, that is, the document that contains the root toctree directive.
# Default is 'index'.

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_**"]
# A list of glob-style patterns that should be excluded when looking for source files. They are matched against the
# source file names relative to the source directory, using slashes as directory separators on all platforms.

include_patterns = ["**"]
# A list of glob-style patterns [1] that are used to find source files. They are matched against the source file names
# relative to the source directory, using slashes as directory separators on all platforms.
# The default is **, meaning that all files are recursively included from the source directory.

templates_path = ["_templates"]
# A list of paths that contain extra templates (or templates that overwrite builtin/theme-specific templates).
# Relative paths are taken as relative to the configuration directory.

rst_epilog = ""
# A string of reStructuredText that will be included at the end of every source file that is read. This is a possible
# place to add substitutions that should be available in every file (another being rst_prolog).
# An example: rst_epilog = """.. |psf| replace:: Python Software Foundation"""

rst_prolog = ""
# A string of reStructuredText that will be included at the beginning of every source file that is read.
# This is a possible place to add substitutions that should be available in every file (another being rst_epilog).
# An example: rst_epilog = """.. |psf| replace:: Python Software Foundation"""

primary_domain = "py"
# The name of the default domain. Can also be None to disable a default domain. The default is 'py'.

default_role = "py:obj"
# The name of a reST role (builtin or Sphinx extension) to use as the default role, that is, for text marked up
# `like this`. This can be set to 'py:obj' to make `filter` a cross-reference to the Python function “filter”.
# The default is None, which doesn't reassign the default role.

keep_warnings = False
# If true, keep warnings as “system message” paragraphs in the built documents. Regardless of this setting,
# warnings are always written to the standard error stream when sphinx-build is run. The default is False.

suppress_warnings = []
# A list of warning types to suppress arbitrary warning messages.

needs_sphinx = "6.1"
# If set to a major.minor version string like '1.1',
# Sphinx will compare it with its version and refuse to build if it is too old. Default is no requirement.

needs_extensions = {}
# This value can be a dictionary specifying version requirements for extensions in extensions, e.g.
# needs_extensions = {'sphinxcontrib.something': '1.5'}. The version strings should be in the form major.minor.
# Requirements do not have to be specified for all extensions, only for those you want to check.

nitpicky = False
# If true, Sphinx will warn about all references where the target cannot be found. Default is False.
# You can activate this mode temporarily using the -n command-line switch.

smartquotes = True
# If true, the Docutils Smart Quotes transform, originally based on SmartyPants (limited to English) and currently
# applying to many languages, will be used to convert quotes and dashes to typographically correct entities.
# Default: True.

pygments_style = "default"
# The style name to use for Pygments highlighting of source code.
# If not set, either the theme’s default style or 'sphinx' is selected for HTML output.

add_function_parentheses = False
# A boolean that decides whether parentheses are appended to function and method role text
# (e.g. the content of :func:`input`) to signify that the name is callable. Default is True.

add_module_names = False
# A boolean that decides whether module names are prepended to all object names
# (for object types where a “module” of some kind is defined), e.g. for py:function directives. Default is True.

show_authors = True
# A boolean that decides whether codeauthor and sectionauthor directives produce any output in the built files.

python_use_unqualified_type_names = True
# If true, suppress the module name of the python reference if it can be resolved. The default is False

# endregion General Configuration -------------------------------------------------------------------------------------

# region HTML Configuration ------------------------------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_style=???
# The style sheet to use for HTML pages. A file of that name must exist either in Sphinx’s static/ path,
# or in one of the custom paths given in html_static_path. Default is the stylesheet given by the selected theme.
# If you only want to add or override a few things compared to the theme’s stylesheet,
# use CSS @import to import the theme’s stylesheet.

html_title = f"{MODULE} {VERSION}"
# The “title” for HTML documentation generated with Sphinx’s own templates.
# This is appended to the <title> tag of individual pages, and used in the navigation bar as the “topmost” element.
# It defaults to '<project> v<revision> documentation'.

html_short_title = MODULE
# A shorter “title” for the HTML docs. This is used for links in the header and in the HTML Help docs.
# If not given, it defaults to the value of html_title.

html_baseurl = ""
# The base URL which points to the root of the HTML documentation.
# It is used to indicate the location of document using The Canonical Link Relation. Default: ''.

html_context = {}
# A dictionary of values to pass into the template engine’s context for all pages.
# Single values can also be put in this dictionary using the -A command-line option of sphinx-build.

html_logo = None
# If given, this must be the name of an image file (path relative to the configuration directory)
# that is the logo of the docs, or URL that points an image file for the logo. It is placed at the top of the sidebar;
# its width should therefore not exceed 200 pixels. Default: None.

html_favicon = None
# If given, this must be the name of an image file (path relative to the configuration directory) that is the favicon
# of the docs, or URL that points an image file for the favicon.
# Modern browsers use this as the icon for tabs, windows and bookmarks.
# It should be a Windows-style icon file (.ico), which is 16x16 or 32x32 pixels large. Default: None.

html_static_path = ["_static"]
# A list of paths that contain custom static files (such as style sheets or script files).
# Relative paths are taken as relative to the configuration directory. They are copied to the output’s _static
# directory after the theme’s static files, so a file named default.css will overwrite the theme’s default.css.

html_extra_path = []
# A list of paths that contain extra files not directly related to the documentation, such as robots.txt or .htaccess.
# Relative paths are taken as relative to the configuration directory. They are copied to the output directory.
# They will overwrite any existing file of the same name.

html_use_smartypants = True
# If true, quotes and dashes are converted to typographically correct entities. Default: True.

html_permalinks = True
# If true, Sphinx will add “permalinks” for each heading and description environment. Default: True.

html_permalinks_icon = "§"
# A text for permalinks for each heading and description environment. HTML tags are allowed. Default: a paragraph sign;

html_sidebars = {}
# Custom sidebar templates, must be a dictionary that maps document names to template names.

# TODO: Add missing configuration options.

# endregion HTML Configuration ---------------------------------------------------------------------------------


# region sphinx-autoapi configuration ---------------------------------------------------------------------------------
# https://github.com/readthedocs/sphinx-autoapi

autoapi_dirs = [f"../{MODULE_DIR}"]
# Paths (relative or absolute) to the source code that you wish to generate your API documentation from.

autoapi_type = "python"
# Set the type of files you are documenting. This depends on the programming language that you are using.
# Default: "python"

autoapi_template_dir = "_templates/autoapi"
# A directory that has user-defined templates to override our default templates. The path can either be absolute,
# or relative to the source directory of your documentation files. A path relative to where sphinx-build is run is
# allowed for backwards compatibility only and will be removed in a future version.
# Default: ""

autoapi_file_patterns = ["*.py", "*.pyi"]
# A list containing the file patterns to look for when generating documentation.
# Patterns should be listed in order of preference. For example, if autoapi_file_patterns is set to the default value,
# and a .py file and a .pyi file are found, then the .py will be read.

autoapi_generate_api_docs = True
# Whether to generate API documentation. If this is False, documentation should be generated though the Directives.
# Default: True

# autoapi_options = [
#     # "members",
#     # "special-members",
#     "imported-members",
#     # "undoc-members",
#     # "private-members",
#     # "show-inheritance",
#     # "show-module-summary",
# ]
# Options for display of the generated documentation.
# Default: [ 'members', 'undoc-members', 'private-members', 'show-inheritance', 'show-module-summary',
# 'special-members', 'imported-members', ]

autoapi_ignore = ["*migrations*"]
# A list of patterns to ignore when finding files. The defaults by language are:
# Default = ['*migrations*']

autoapi_root = "autoapi"
# Path to output the generated AutoAPI files into, including the generated index page.
# This path must be relative to the source directory of your documentation files.
# This can be used to place the generated documentation anywhere in your documentation hierarchy.
# Default: "autoapi"

autoapi_add_toctree_entry = False
# Whether to insert the generated documentation into the TOC tree. If this is False, the default AutoAPI index page
# is not generated, and you will need to include the generated documentation in a TOC tree entry yourself.
# Default: True

autoapi_member_order = "groupwise"
# The order to document members. This option can have the following values:
# alphabetical: Order members by their name, case sensitively.
# bysource: Order members by the order that they were defined in the source code.
# groupwise: Order members by their type then alphabetically, ordering the types as follows:
# Submodules and subpackages, Attributes, Exceptions, Classes, Functions, and Methods.
# Default: bysource

autoapi_python_class_content = "both"
# Which docstring to insert into the content of a class.
# If the class does not have an __init__ or the __init__ docstring is empty and
# the class defines a __new__ with a docstring, the __new__ docstring is used instead of the __init__ docstring.
# Default: "class"

autoapi_python_use_implicit_namespaces = True
# This changes the package detection behaviour to be compatible with PEP 420,
# but directories in autoapi_dirs are no longer searched recursively for packages. Instead, when this is True,
# autoapi_dirs should point directly to the directories of implicit namespaces and the directories of packages.
# Default: False

autoapi_prepare_jinja_env = None
# A callback that is called shortly after the Jinja environment is created.
# It passed the Jinja environment for editing before template rendering begins.
# Default: None

autoapi_keep_files = True
# Keep the AutoAPI generated files on the filesystem after the run.
# Useful for debugging or transitioning to manual documentation.
# Keeping files will also allow AutoAPI to use incremental builds. Providing none of the source files have changed,
# AutoAPI will skip parsing the source code and regenerating the API documentation.
# Default: False

# endregion sphinx-autoapi configuration ------------------------------------------------------------------------------


# region sphinx_math_dollar configuration ------------------------------------------------------------------------------

# https://www.sympy.org/sphinx-math-dollar/#configuration
# from sphinx_math_dollar import NODE_BLACKLIST
# from docutils.nodes import header
# from sphinx.addnodes import pending_xref_condition
# math_dollar_debug = True
# math_dollar_node_blacklist = NODE_BLACKLIST + (header, pending_xref_condition)


# endregion sphinx_math_dollar configuration ---------------------------------------------------------------------------


# -- end of configuration ---------------------------------------------------------------------------------------------
