# Python 2.7.4.

import unittest
import Points
import math

class TestTime(unittest.TestCase):

    def setUp(self):
        self.point0 = Points.Point(0, 0)
        self.point1 = Points.Point(1, 1)
        self.point1bis = Points.Point(1, 1)
        self.point2 = Points.Point(1, 2)

    def test_print(self):      # test str() i repr()
        self.assertEqual(self.point1.__str__(), '(1, 1)')
        self.assertEqual(self.point1.__repr__(), 'Point(1, 1)')

    def test_eq(self):
        self.assertTrue(self.point1 == self.point1bis)
        self.assertFalse(self.point1 == self.point0)

    def test_ne(self):
        self.assertFalse(self.point1 != self.point1bis)
        self.assertTrue(self.point1 != self.point0)

    def test_add(self):
        self.assertEqual(self.point1 + self.point2, Points.Point(2, 3))

    def test_sub(self):
        self.assertEqual(self.point1 - self.point2, Points.Point(0, -1))

    def test_mul(self):
        self.assertEqual(self.point1 * self.point2, 3)

    def test_cross(self):
        self.assertEqual(self.point1.cross(self.point2), 1)

    def test_length(self):
        self.assertEqual(self.point2.length(), math.sqrt(5))
        self.assertEqual(self.point0.length(), 0)

    def tearDown(self):
        self.point0 = None
        self.point1 = None
        self.point1bis = None
        self.point2 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy