# Python 2.7.4.

import unittest


class TestTime(unittest.TestCase):

    def setUp(self):
        self.C0 = circles.Circle()

    def test_points_radius(self):      # test punktow i promienia
        self.assertEqual(self.C0.pt, self.p00)

    def test_eq(self):
        self.assertTrue(self.C0 == self.C0prim)
        self.assertFalse(self.C0 == self.C112)

    def tearDown(self):
        self.C0 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy