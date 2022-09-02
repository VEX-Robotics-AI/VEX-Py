"""Sphinx Documentation Configurations."""


# Configuration file for the Sphinx documentation builder.

# This file only contains a selection of the most common options.
# For the full list of built-in configuration values, see the documentation:
# sphinx-doc.org/en/master/usage/configuration.html


from datetime import date
from importlib.metadata import metadata
import os

import vex


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
# sphinx-doc.org/en/master/usage/configuration.html#project-information

METADATA: dict[str, str] = metadata(distribution_name='VEX-Py')

project: str = METADATA['Name']
author: str = METADATA['Author']

# pylint: disable=redefined-builtin
copyright: str = f'{date.today().year}, {author}'

# The full version, including alpha/beta/rc tags
release: str = vex.__version__


# -- General configuration ---------------------------------------------------
# sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named 'sphinx.ext.*')
# or your custom ones.
extensions: list[str] = [
    'sphinx.ext.autodoc',   # Include documentation from docstrings
    'sphinx.ext.autosectionlabel',   # Allow reference sections using its title
    'sphinx.ext.autosummary',   # Generate autodoc summaries

    'sphinx.ext.coverage',   # Collect doc coverage stats
    'sphinx.ext.doctest',   # Test snippets in the documentation
    'sphinx.ext.duration',   # Measure durations of Sphinx processing
    'sphinx.ext.extlinks',   # Markup to shorten external links
    'sphinx.ext.githubpages',   # Publish HTML docs in GitHub Pages
    'sphinx.ext.graphviz',   # Add Graphviz graphs
    'sphinx.ext.ifconfig',   # Include content based on configuration
    'sphinx.ext.imgconverter',   # reference image converter using Imagemagick
    'sphinx.ext.inheritance_diagram',   # Include inheritance diagrams
    'sphinx.ext.intersphinx',   # Link to other projects’ documentation
    # 'sphinx.ext.linkcode',   # Add external links to source code
    # TODO: provide linkcode_resolve function

    'sphinx.ext.imgmath',   # Render math as images
    'sphinx.ext.mathjax',   # Render math via JavaScript
    'sphinxcontrib.jsmath',   # Render math via JavaScript

    'sphinx.ext.napoleon',   # Support for NumPy and Google style docstrings
    'sphinx.ext.todo',   # Support for todo items
    'sphinx.ext.viewcode',   # Add links to highlighted source code

    'myst_parser',
]

# Add any paths that contain templates here, relative to this directory.
templates_path: list[str] = ['_templates']

# List of patterns, relative to source directory,
# that match files and directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: list[str] = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.
# See the documentation for a list of builtin themes.
html_theme: str = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path: list[str] = ['_static']

for _html_static_path in html_static_path:
    os.makedirs(name=_html_static_path, exist_ok=True)


# Math rRnderer
html_math_renderer: str = 'mathjax'


# Source Parsers
source_suffix: dict[str, str] = {'.md': 'markdown', '.rst': 'restructuredtext'}
