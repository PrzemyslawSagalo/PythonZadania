# Python 2.7.4

import unittest
import circles
import Points
import math

class TestCircles(unittest.TestCase):

    def setUp(self):
        self.C0 = circles.Circle()
        self.C0prim = circles.Circle()
        self.C112 = circles.Circle(1, 1, 2)

        self.p00 = Points.Point(0,0)
        self.p11 = Points.Point(1,1)

    def test_points_radius(self):      # test punktow i promienia
        self.assertEqual(self.C0.pt, self.p00)
        self.assertEqual(self.C0.radius, 1)

        with self.assertRaises(ValueError):
            circles.Circle(1, 1, -1)

    def test_repr(self):
        self.assertEqual(repr(self.C0), "Circle(0, 0, 1)")

    def test_eq(self):
        self.assertTrue(self.C0 == self.C0prim)
        self.assertFalse(self.C0 == self.C112)

    def test_ne(self):
        self.assertFalse(self.C0 != self.C0prim)
        self.assertTrue(self.C112 != self.C0)

    def test_area(self):
        self.assertEqual(self.C0.area(), math.pi)
        self.assertEqual(self.C112.area(), math.pi * 4)

    def test_move(self):
        self.C0.move(1, 1)
        self.assertEqual(self.C0.pt, Points.Point(1,1))
        self.C0.move(1,-1)
        self.assertEqual(self.C0.pt, Points.Point(2,0))

    # def test_cover(self):
    #     self.assertEqual(circles.Circle(1,1,5).cover(self.C0), circles.Circle(0, 0, 6))

    def tearDown(self):
        self.C0 = None
        self.C0prim = None
        self.C112 = None

        self.p00 = None
        self.p11 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy