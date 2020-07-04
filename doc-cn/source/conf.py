# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import logging


# -- Project information -----------------------------------------------------
project = 'Arctern'
copyright = '2020, zilliz'
author = 'zilliz'

logger = logging.getLogger(__name__)

# The full version, including alpha/beta/rc tags
import arctern
release = arctern.version()


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
   'sphinx.ext.autodoc',
   'sphinx.ext.viewcode',
   'sphinx_automodapi.automodapi',
   'sphinx.ext.inheritance_diagram',
   'sphinx.ext.autosummary',
   'sphinx_markdown_tables',
   'matplotlib.sphinxext.plot_directive',
   'recommonmark',
   'sphinx.ext.napoleon'
]

exclude_patterns = ["**.ipynb_checkpoints"]
try:
    import nbconvert
except ImportError:
    logger.warn("nbconvert not installed. Skipping notebooks.")
    exclude_patterns.append("**/*.ipynb")
else:
    try:
        nbconvert.utils.pandoc.get_pandoc_version()
    except nbconvert.utils.pandoc.PandocMissing:
        logger.warn("Pandoc not installed. Skipping notebooks.")
        exclude_patterns.append("**/*.ipynb")

plot_include_source = True
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False
plot_pre_code = """import numpy as np
import pandas as pd"""

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'
locale_dirs = ['locale/'] # path is example but recommended.
gettext_compact = False # optional.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#add_module_names = False
html_last_updated_fmt = '%b %d, %Y'
html_domain_indices = True
html_theme = 'sphinx_rtd_theme'
#html_logo = './_static/arctern-color.png'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
