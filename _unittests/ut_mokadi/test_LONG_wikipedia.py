# -*- coding: utf-8 -*-
"""
@brief      test log(time=40s)
"""

import sys
import os
import unittest
import wikipedia


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


from src.jupytalk.mokadi import definition_wikipedia, suggestions_wikipedia, synonyms_wiktionary


class TestWikipedia(unittest.TestCase):

    def test_wikipedia_summary(self):
        res = definition_wikipedia("microsoft")
        self.assertTrue("Gates" in res)
        res = definition_wikipedia("intelligence")
        self.assertTrue("L'intelligence" in res)
        try:
            definition_wikipedia("intelligence iafhaepzfuichaefhanozfnhaoi")
            raise AssertionError("should fail")
        except wikipedia.exceptions.PageError:
            pass

    def test_wikipedia_definition(self):
        res = definition_wikipedia("intelligence", summary=False)
        enc = res.encode("utf-8")
        dec = enc.decode("cp1252", errors="ignore")
        self.assertTrue(dec)

    def test_suggestion(self):
        res = suggestions_wikipedia("pari")
        self.assertTrue(isinstance(res, list))
        self.assertTrue(len(res) > 0)

    def test_dictionary_synonym(self):
        res = synonyms_wiktionary("ville")
        self.assertTrue(isinstance(res, list))
        self.assertEqual(len(res), 1)

    def test_dictionary_synonym_travail(self):
        res = synonyms_wiktionary("travail")
        self.assertTrue(isinstance(res, list))
        self.assertEqual(len(res), 10)
        self.assertEqual(res, ['boulot', 'chagrin', 'emploi', 'gagne-pain',
                               'job', 'métier', 'profession', 'job', 'taf', 'turbin'])


if __name__ == "__main__":
    unittest.main()
