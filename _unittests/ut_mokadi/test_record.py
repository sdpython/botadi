# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor, get_temp_folder


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


from src.jupytalk.mokadi import record_speech, play_speech


class TestRestApiSpeech(unittest.TestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_record(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fLOG("record")
        temp = get_temp_folder(__file__, "temp_record")
        output = os.path.join(temp, "output.wav")
        try:
            record = record_speech(3, fLOG=fLOG, WAVE_OUTPUT_FILENAME=output)
        except Exception as e:
            raise Exception("Does not work") from e
        fLOG("play", len(record))
        play_speech(record)
        fLOG("end")


if __name__ == "__main__":
    unittest.main()
