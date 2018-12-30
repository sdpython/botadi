# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
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


from src.jupytalk.mokadi import enumerate_last_mails


class TestMail(unittest.TestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_mail(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            import keyring
        user = keyring.get_password("gmail", "jupytalk,user")
        pwd = keyring.get_password("gmail", "jupytalk,pwd")
        server = "imap.gmail.com"
        try:
            mails = enumerate_last_mails(user, pwd, server, fLOG=fLOG)

            i = 0
            for mail in mails:
                fLOG(mail.get_name(), "**", mail.get_nb_attachements(),
                     "**", mail.get_date_str())
                fLOG(mail.get_field("subject").split("\n")[0])
                i += 1

        except Exception as e:
            raise Exception("Does not work") from e


if __name__ == "__main__":
    unittest.main()
