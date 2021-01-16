# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""
import unittest
import warnings
from pyquickhelper.loghelper import fLOG, get_password
from pyquickhelper.pycode import is_travis_or_appveyor
from botadi.mokadi import enumerate_last_mails


class TestMail(unittest.TestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_mail(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        user = get_password("gmail", "botadi,user")
        pwd = get_password("gmail", "botadi,pwd")
        if user is None:
            raise ValueError("user is not specified.")
        if pwd is None:
            warnings.warn("pwd is not specified.")
            return
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
