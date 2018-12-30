# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor


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
from src.jupytalk.mokadi.mokadi_action_emotion import MokadiActionEmotion
from src.jupytalk.mokadi.mokadi_action_conversation import MokadiActionConversation
from src.jupytalk.mokadi.grammars import MokadiGrammar_frParser, MokadiGrammar_frLexer, MokadiGrammar_frListener
from src.jupytalk.mokadi.mokadi_exceptions import CognitiveException


class TestEngineExtended_2(unittest.TestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no keys")
    def test_engine_ex_2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_engine_ex_2")
        clog = fLOG

        fLOG("Adding actions with credentials.")
        messages = ["MOKADI bonjour"]

        actions = [MokadiActionConversation(fLOG=fLOG),
                   ]

        # Adding test which requires credentials.
        fLOG("Adding actions with credentials.")
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            import keyring
        subkey_emo = keyring.get_password("cogser", "jupytalk,emotions")
        messages.append("MOKADI humeur")
        actions.insert(0, MokadiActionEmotion(subkey_emo, temp, fLOG=fLOG))

        # Test is beginning.
        engine = MokadiEngine(temp, clog, actions, MokadiGrammar_frParser,
                              MokadiGrammar_frLexer, MokadiGrammar_frListener)
        verif = 0
        for text in messages:
            fLOG("***", text)
            mes = MokadiMessage(text, 1)
            try:
                res = list(engine.process(mes, exc=True))
            except CognitiveException:
                warnings.warn("Unable to process '{0}'".format(text))
                continue
            fLOG(res)
            self.assertTrue(len(res) > 0)
            verif += 1
        self.assertTrue(verif > 0)


if __name__ == "__main__":
    unittest.main()
