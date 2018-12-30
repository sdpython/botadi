# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor, add_missing_development_version


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


class TestSpeak(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["jyquickhelper", "ensae_teaching_cs", "pymmails"],
                                        __file__, hide=True)

    def test_speak(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # no keys
            return

        from src.jupytalk.mokadi import speak

        try:
            speak("mail reçu à 15h30 mardi 21 septembre.")
        except NotImplementedError:
            warnings.warn("Speech not implemented")
        except Exception as e:
            if "Audio device error encountered" in str(e) or \
                    "Erreur de périphérique audio rencontrée" in str(e):
                # maybe the script is running on a virtual machine (no
                # Audia device)
                if os.environ["USERNAME"] == "ensaestudent" or \
                   os.environ["USERNAME"] == "vsxavierdupre" or \
                   os.environ["USERNAME"] == "vsxavierdupre" or \
                   os.environ["USERNAME"] == "Administrateur" or \
                   "DOUZE2016" in os.environ.get("COMPUTERNAME", "") or \
                   os.environ["USERNAME"] == "appveyor" or \
                   "ENSAE" in os.environ.get("COMPUTERNAME", "") or \
                   os.environ["USERNAME"].endswith("$"):  # anonymous Jenkins configuration
                    # I would prefer to catch a proper exception
                    # it just exclude one user only used on remotre
                    # machines
                    return
            raise Exception("Audio device should work") from e


if __name__ == "__main__":
    unittest.main()
