# Python 2.7.4

import unittest
import Points

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

        self.assertTrue(self.point1.__eq__(self.point1bis))
        self.assertFalse(self.point1.__eq__(self.point0))


    def tearDown(self):
        self.point1 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy