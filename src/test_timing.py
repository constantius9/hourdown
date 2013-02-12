#! /usr/bin/env python

"""This is a test for general program facilities."""

import unittest


class FacilitiesTest(unittest.TestCase):
    def testFactorADayFullScheme(self):
        day = Day()
        schema = '8h-2×2h:4×1h:8×30m:16×15m'
        day.factor(schema)
        self.assertEqual(len(day.slots['2h']), 2)
        self.assertEqual(len(day.slots['1h']), 4)
        self.assertEqual(len(day.slots['30m']), 8)
        self.assertEqual(len(day.slots['15m']), 16)
        self.assertEqual(day.sleep, '8h')

    def testFactorADayContractedScheme(self):
        day = Day()
        schema = '2×2h:4×1h:8×30m:16×15m'
        day.factor(schema)
        self.assertEqual(len(day.slots['2h']), 2)
        self.assertEqual(len(day.slots['1h']), 4)
        self.assertEqual(len(day.slots['30m']), 8)
        self.assertEqual(len(day.slots['15m']), 16)
        self.assertEqual(day.sleep, '8h')


if __name__ == '__main__':
    unittest.main()