# -*- coding: utf-8 -*-
"""
@brief      test log(time=5s)
"""
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG, get_password
from pyquickhelper.pycode import is_travis_or_appveyor
from botadi.mokadi.cognitive_services_helper import call_api_emotions


class TestRestApiEmotions(unittest.TestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_api_emotions(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
        imgs = [os.path.join(path, "84-cate-blanchett-jude-quinn-i-m-not-there-2007--630-75.jpg"),
                os.path.join(path, "Cate_Blanchett_Deauville_2013_2.jpg")]

        subkey = get_password("cogser", "botadi,emotions")
        if not subkey:
            warnings.warn("No key")
            return
        for img in imgs:
            res = call_api_emotions(subkey, img)
            if isinstance(res, dict):
                error = res.get('error', None)
                if error is not None:
                    if error.get('statusCode', 200) == 404:
                        warnings.warn("Key should be checked or renewed.")
                        continue
            if not isinstance(res, list):
                if "Resource not found" in str(res):
                    warnings.warn("API changed, it should be updated.")
                    return
                else:
                    raise TypeError('{}\n{}'.format(type(res), res))
            self.assertTrue(len(img) > 0)
            for _ in res:
                fLOG(_)


if __name__ == "__main__":
    unittest.main()
