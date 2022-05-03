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
import os
import sys
# sys.path.insert(0, os.path.abspath('../..'))
# Standard code

# Assumption: the conf.py file is in the root_of_project > docs > source
# ../../ Then brings us back to the root of the project.

# Working version for one file
# sys.path.insert(0, os.path.abspath('../../src/'))
# manually add all the paths to the folders with python files

# ##### -> Code for the following structure of code folder:
# folder with app.py and then all the folders other code files in this folder
# or in sub-folders underneath the src folder

directory = '../../src/'
# How to get from the conf.py file to the code

# Add the app.py to the sys.path which the conf.py file needs to make automatic documentation
sys.path.insert(0, os.path.abspath('../../src/'))

# Add all sub-folders in the src folder which contain the python files
# This way all the python files can be accessed.
for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        sys.path.insert(0, os.path.abspath(os.path.join(root, subdirectory)))
    for file in files:
        # print(os.path.join(root, file))
        pass

print(sys.path)

# -- Project information -----------------------------------------------------

project = 'Avocado Analytics'
copyright = '2022, JH'
author = 'JH'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'numpydoc', 'sphinx.ext.autosummary', 'sphinx.ext.viewcode' #'sphinx.ext.napoleon',  # evt 'numpydoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']