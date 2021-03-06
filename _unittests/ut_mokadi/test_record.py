# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import (
    is_travis_or_appveyor, get_temp_folder, ExtTestCase)
from botadi.mokadi import record_speech, play_speech


class TestRestApiSpeech(ExtTestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_record(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        try:
            import pyaudio
        except ImportError:
            warnings.warn("pyaudio is missing.")
            return
        self.assertNotEmpty(pyaudio)
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
