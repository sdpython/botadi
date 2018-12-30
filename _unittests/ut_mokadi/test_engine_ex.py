# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, ExtTestCase


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


from src.jupytalk.mokadi import MokadiEngine, MokadiMessage
from src.jupytalk.mokadi.mokadi_action_slides import MokadiActionSlides
from src.jupytalk.mokadi.mokadi_action_conversation import MokadiActionConversation
from src.jupytalk.mokadi.mokadi_action_mail import MokadiActionMail
from src.jupytalk.mokadi.mokadi_action_news import MokadiActionNews
from src.jupytalk.mokadi.grammars import MokadiGrammar_frParser, MokadiGrammar_frLexer, MokadiGrammar_frListener


class TestEngineExtended(ExtTestCase):

    def test_engine_ex(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_engine_ex")
        clog = fLOG
        folder = os.path.join(temp, "..", "data")

        fLOG("Adding actions with credentials.")
        messages = ["MOKADI liste presentation",
                    "MOKADI lire presentation 1 slide 2",
                    "MOKADI lire presentation 1 slide numéro 2",
                    "MOKADI hello",
                    "MOKADI bruit de toilette",
                    "MOKADI définition de la tour eiffel",
                    "MOKADI c'est quoi la tour eiffel",
                    "MOKADI synonymes de ville",
                    ]

        actions = [MokadiActionSlides(folder, fLOG=fLOG),
                   MokadiActionConversation(fLOG=fLOG),
                   ]

        # Adding test which requires credentials.
        if not is_travis_or_appveyor():
            fLOG("Adding actions with credentials.")
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', DeprecationWarning)
                import keyring
            user = keyring.get_password("gmail", "jupytalk,user")
            pwd = keyring.get_password("gmail", "jupytalk,pwd")
            server = "imap.gmail.com"
            subkey_news = keyring.get_password("cogser", "jupytalk,news")
            if subkey_news is None:
                warnings.warn("No key")
                return

            messages.append("MOKADI lire mail 2 en entier")
            messages.append("MOKADI lire mail 2")
            messages.append("MOKADI lire mail numéro 2")
            messages.append("MOKADI lire 1 mail")
            messages.append("MOKADI lire un mail")
            messages.append("MOKADI lire mail")
            messages.append("MOKADI lire news")
            messages.append("MOKADI lire news sur les élections")

            actions.insert(0, MokadiActionMail(
                user=user, pwd=pwd, server=server, fLOG=fLOG))
            actions.insert(0, MokadiActionNews(subkey_news, fLOG=fLOG))

        # Test is beginning.
        engine = MokadiEngine(temp, clog, actions, MokadiGrammar_frParser,
                              MokadiGrammar_frLexer, MokadiGrammar_frListener)
        verif = 0
        for i, text in enumerate(messages):
            fLOG("***", text)
            mes = MokadiMessage(text, 1)
            res = list(engine.process(mes, exc=True))
            if len(res) == 0:
                continue
            self.assertNotEmpty(res)
            if i == 4:
                self.assertEqual(len(res), 1)
                self.assertTrue(res[0].has_sound)
                verif += 1
        self.assertTrue(verif > 0)


if __name__ == "__main__":
    unittest.main()
