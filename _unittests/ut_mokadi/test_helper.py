# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""
import unittest
import datetime
from botadi.mokadi.mokadi_helper import convert_into_days


class TestHelper(unittest.TestCase):

    def test_helper(self):
        r = "2017-04-03T12:58:00"
        conv = convert_into_days(r)
        self.assertTrue(isinstance(conv, str))

        now = datetime.datetime.now()
        r1 = convert_into_days(now + datetime.timedelta(1))
        self.assertEqual(r1, "dans le futur")
        r1 = convert_into_days(now + datetime.timedelta(0))
        self.assertEqual(r1, "il y a moins d'une heure")
        r1 = convert_into_days(now - datetime.timedelta(hours=1))
        self.assertEqual(r1, "il y a moins d'une heure")
        r1 = convert_into_days(now - datetime.timedelta(hours=14))
        self.assertEqual(r1, "aujourd'hui")
        r1 = convert_into_days(now - datetime.timedelta(1))
        self.assertEqual(r1, "hier")
        r1 = convert_into_days(now - datetime.timedelta(2))
        self.assertEqual(r1, "avant-hier")
        r1 = convert_into_days(now - datetime.timedelta(3))
        self.assertEqual(r1, "il y a 3 jours")


if __name__ == "__main__":
    unittest.main()
