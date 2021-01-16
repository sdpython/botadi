# -*- coding: utf-8 -*-
"""
@brief      test log(time=5s)
"""
import unittest
import warnings
from pyquickhelper.loghelper import fLOG, get_password
from pyquickhelper.pycode import is_travis_or_appveyor
from botadi.mokadi.cognitive_services_helper import call_api_news


class TestRestApiNews(unittest.TestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_api_news(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        subkey = get_password("cogser", "botadi,news")
        if not subkey:
            warnings.warn("No key")
            return
        res = call_api_news(subkey, "tennis")
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
