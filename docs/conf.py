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
import shutil

from pathlib import Path

# -- Project information -----------------------------------------------------

project = 'mypackage'
copyright = '2022, Jake'
author = 'Jake'

# The full version, including alpha/beta/rc tags
release = '0.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "sphinxcontrib.apidoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

apidoc_module_dir = f"../{project}"
apidoc_excluded_paths = ["tests"]
apidoc_toc_file = False

autodoc_default_options = {"members": True}
autodoc_member_order = "bysource"
autoclass_content = "init"

language="en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    print("\nSetting up custom extension\n")
    here = Path(__file__).resolve().parent
    doc_examples = here / "examples"
    if not doc_examples.exists():
        (here / "examples").mkdir()
    example_source = (here / "../examples").resolve()
    source_notebooks  = example_source.glob("**/*.ipynb")
    shutil.copy(example_source / "README.rst", doc_examples / "index.rst")
    for notebook in source_notebooks:
        # This part is specific to our notebook directory structure
        new_dir = doc_examples / notebook.parent.stem
        new_dir.mkdir(exist_ok=True)
        new_file =  new_dir / "example.ipynb"
        print(f"Creating file {new_file}")
        shutil.copy(notebook, new_file)
    

