# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
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

from src.jupytalk.mokadi import take_picture


class TestPicture(unittest.TestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_take_picture(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_take_picture")

        for module in ["pygame", "cv2"]:
            fLOG(module)
            img = os.path.join(temp, "im_{0}.png".format(module))
            try:
                take_picture(img, module=module)
            except Exception as e:
                warnings.warn(
                    "Fails with module '{0}' - {1}".format(module, e))


if __name__ == "__main__":
    unittest.main()
