# -*- coding: utf-8 -*-
import sys
import os
import sphinx_modern_theme_modified
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "botadi", "Xavier Dupré", 2018,
                     "sphinx_modern_theme_modified", sphinx_modern_theme_modified.get_html_theme_path(),
                     locals(), extlinks=dict(
                         issue=('https://github.com/sdpython/botadi/issues/%s', 'issue')),
                     github_user="sdpython", github_repo="botadi", book=True)

blog_root = "http://www.xavierdupre.fr/app/botadi/helpsphinx/"
blog_background = False
html_context = {
    'css_files': get_default_stylesheet() + ['_static/my-styles.css'],
}

# https://github.com/peterhudec/foundation-sphinx-theme
# http://docs.guzzlephp.org/en/latest/
# http://sphinx-better-theme.readthedocs.io/en/latest/

epkg_dictionary.update({
    'Microsoft': 'https://docs.microsoft.com/en-us/',
})
