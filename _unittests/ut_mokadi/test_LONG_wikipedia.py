# -*- coding: utf-8 -*-
"""
@brief      test log(time=40s)
"""
import unittest
import wikipedia
from botadi.mokadi import definition_wikipedia, suggestions_wikipedia, synonyms_wiktionary


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
        self.assertEqual(len(res), 9)
        ans1 = ['boulot', 'chagrin', 'emploi', 'gagne-pain',
                'job', 'métier', 'profession', 'taf', 'turbin']
        self.assertEqual(res, ans1)


if __name__ == "__main__":
    unittest.main()
