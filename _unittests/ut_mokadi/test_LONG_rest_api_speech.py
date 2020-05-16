# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor, add_missing_development_version


class TestLONGRestApiSpeech(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["jyquickhelper", "pymmails"],
                                        __file__, hide=True)

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_api_speech_reco(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from botadi.mokadi.cognitive_services_helper import call_api_speech_reco
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            import keyring
        subkey = keyring.get_password("cogser", "botadi,voicereco")
        if not subkey:
            warnings.warn("no key")
            return

        wav = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), "data", "output.wav")
        with open(wav, "rb") as f:
            content = f.read()

        try:
            res = call_api_speech_reco(subkey, memwav=content)
        except NotImplementedError:
            # removed
            return
        fLOG(res)
        self.assertTrue(isinstance(res, dict))
        for k, v in res.items():
            fLOG(k, v)
            if "results" == k:
                for _ in v:
                    fLOG(_)

        # returns something like
        # {'header': {'properties': {'requestid': '88af3c3f-3288-49f8-9dc3-4e0a30c9e97e', 'HIGHCONF': '1'},
        #                            'status': 'success',
        #                            'lexical': 'leocadie va chercher email',
        #                            'name': 'Leocadie va chercher email.', 'scenario': 'smd'},
        # 'results': [{'properties': {'HIGHCONF': '1'}, 'confidence': '0.6540837',
        #              'lexical': 'leocadie va chercher email',
        #              'name': 'Leocadie va chercher email.', 'scenario': 'smd'}],
        # 'version': '3.0'}


if __name__ == "__main__":
    unittest.main()
