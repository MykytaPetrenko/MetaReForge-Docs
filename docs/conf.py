# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from recommonmark.transform import AutoStructify

def setup(app):
    app.add_transform(AutoStructify)

project = 'MetaReForge Docs'
copyright = '2023, Sqeezy Pixels (Mykyta Petrenko)'
author = 'Sqeezy Pixels (Mykyta Petrenko)'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_extra_path = ['images']

extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'
project = "MetaReForge"

# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "MetaReForge",
    logo = "img/mrf_logo.svg",
    logo_alt = "MetaReForge",
    logo_height = 150,
    logo_url = "https://mykytapetrenko.github.io/MetaReForge-Docs/",
    logo_width = 142,
    github_url = "https://github.com/MykytaPetrenko/MetaReForge-Docs/tree/main/docs/"

)
# extensions.append("sphinx_rtd_theme")
# html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]
