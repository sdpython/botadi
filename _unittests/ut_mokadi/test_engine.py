# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder
from botadi.mokadi import MokadiEngine, MokadiMessage, MokadiInfo
from botadi.mokadi.mokadi_action_slides import MokadiActionSlides
from botadi.mokadi.grammars import MokadiGrammar_frParser, MokadiGrammar_frLexer, MokadiGrammar_frListener


class TestEngine(unittest.TestCase):

    def test_engine_simple(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_engine_simple")
        clog = CustomLog(temp)
        engine = MokadiEngine(temp, clog, [], MokadiGrammar_frParser,
                              MokadiGrammar_frLexer, MokadiGrammar_frListener)
        mes = MokadiMessage("nokadi", 1)
        res = list(engine.process(mes))
        self.assertEqual(len(res), 1)
        self.assertTrue(isinstance(res[0], MokadiInfo))
        fLOG(res[0])

    def test_engine_slides(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_engine_slides")
        clog = CustomLog(temp)
        folder = os.path.join(temp, "..", "data")
        act = MokadiActionSlides(folder)
        engine = MokadiEngine(temp, clog, [act], MokadiGrammar_frParser,
                              MokadiGrammar_frLexer, MokadiGrammar_frListener)
        mes = MokadiMessage("MOKADI liste presentation", 1)
        res = list(engine.process(mes, exc=True))
        self.assertEqual(len(res), 2)
        self.assertTrue(isinstance(res[0], MokadiInfo))
        self.assertTrue(isinstance(res[1], MokadiInfo))
        fLOG(res[0])


if __name__ == "__main__":
    unittest.main()
