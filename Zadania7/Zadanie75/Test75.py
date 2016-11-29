# Python 2.7.4.

import unittest
import circles
import Points

class TestTime(unittest.TestCase):

    def setUp(self):
        self.C0 = circles.Circle()
        self.C112 = circles.Circle(1, 1, 2)

        self.p00 = Points.Point(0,0)
        self.p11 = Points.Point(1,1)

    def test_print(self):      # test punktow i promienia
        self.assertEqual(self.C0.pt, self.p00)
        self.assertEqual(self.C0.radius, 1)

        self.assertRaises(Points.Point(-1,1,1), ValueError)

    # def test_eq(self):
    #     self.assertTrue(self.point0 == self.point1bis)
    #     self.assertFalse(self.point0 == self.point0)

    def tearDown(self):
        self.C0 = None
        self.C112 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy