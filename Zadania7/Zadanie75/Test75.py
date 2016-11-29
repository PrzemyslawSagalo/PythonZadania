# Python 2.7.4.

import unittest
import Points
import math

class TestTime(unittest.TestCase):

    def setUp(self):
        self.point0 = Points.Point(0, 0)

    def test_print(self):      # test str() i repr()
        self.assertEqual(self.point0.__str__(), '(1, 1)')
        self.assertEqual(self.point0.__repr__(), 'Point(1, 1)')

    def test_eq(self):
        self.assertTrue(self.point0 == self.point1bis)
        self.assertFalse(self.point0 == self.point0)

    def tearDown(self):
        self.point0 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy