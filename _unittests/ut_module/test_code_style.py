"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


class TestCodeStyle(ExtTestCase):
    """Test style."""

    def test_src(self):
        "skip pylint"
        self.assertFalse(src is None)

    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG,
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'R0911', 'W0201', 'W070', 'W0622', 'R1702',
                                  'C0111', 'W0703', 'C0200'),
                   neg_pattern='.*MokadiGrammar_((frParser)|(frListener)|(frLexer))[.]py$',
                   skip=["Unable to import 'ensae_teaching_cs.pythonnet'",
                         "treant_wrapper.py:38: W0603",
                         "No name 'imwrite' in module 'cv2'",
                         "No name 'VideoCapture' in module 'cv2'",
                         "pydata2016.py:77: W0612",
                         "mokadi_mails.py:42: W0612",
                         "Unable to import 'pymmails.grabber'",
                         "mokadi_action_slides.py:84: W0612",
                         "gui_mokadi_process.py:13: W0612",
                         "Redefining name 'fLOG' from outer scope",
                         "Access to member 'thread_listen' before its definition",
                         "Instance of 'Exception' has no 'strerror'",
                         "Instance of 'Exception' has no 'errno'",
                         "gui_mokadi.py:129",
                         "gui_mokadi.py:78: W0612",
                         "Unused variable 'ensae_teaching_cs'",
                         "Unable to import 'ensae_teaching_cs'",
                         "Unable to import 'pygame'",
                         "Unable to import 'pygame.camera'",
                         "Unable to import 'cv2'",
                         "Unable to import 'keyring'",
                         "Unable to import 'pyaudio'",
                         ])

    def test_style_test(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*",
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'W0703', 'C0122', 'W0101', 'R1707'),
                   skip=["src' imported but unused",
                         "skip_' imported but unused",
                         "skip__' imported but unused",
                         "skip___' imported but unused",
                         "Unused variable 'skip_'",
                         "imported as skip_",
                         "Unused import src",
                         "Unable to import 'ensae_teaching_cs.pythonnet'",
                         "Redefining name 'path' from outer scope",
                         "Unable to import 'keyring'",
                         ])


if __name__ == "__main__":
    unittest.main()
