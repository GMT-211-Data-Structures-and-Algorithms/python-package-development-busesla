import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'GeoPackage'
author = 'Buse Sila'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
html_theme = 'sphinx_rtd_theme' # Bunu daha sonra 'alabaster' yaparak 2. temayı test edebilirsin.