"""Sphinx Documentation Configurations."""


# Configuration file for the Sphinx documentation builder.

# This file only contains a selection of the most common options.
# For the full list of built-in configuration values, see the documentation:
# sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
# sphinx-doc.org/en/master/usage/configuration.html#project-information

project: str = 'Robot Mesh VEX IQ Python B API Stubs'
copyright: str = '2021, STEAM for Vietnam'   # pylint: disable=redefined-builtin
author: str = 'STEAM for Vietnam'

# The full version, including alpha/beta/rc tags
release: str = '0.0.0.dev0'


# -- General configuration ---------------------------------------------------
# sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named 'sphinx.ext.*')
# or your custom ones.
extensions: list[str] = [
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
