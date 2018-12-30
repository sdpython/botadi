# -*- coding: utf-8 -*-
"""
@brief      test log(time=5s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor


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

from src.jupytalk.mokadi.cognitive_services_helper import call_api_images


class TestRestApiImages(unittest.TestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_api_news(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            import keyring
        subkey = keyring.get_password("cogser", "jupytalk,news")
        if not subkey:
            warnings.warn("No key")
            return
        res = call_api_images(subkey, "arya stark")
        self.assertTrue(isinstance(res, dict))
        self.assertTrue(len(res) > 0)
        for k, v in res.items():
            fLOG("k={0}".format(k))
            if isinstance(v, list):
                for _ in v:
                    fLOG(_)
                    self.assertTrue(isinstance(_, dict))
                    self.assertTrue("name" in _)


if __name__ == "__main__":
    unittest.main()
