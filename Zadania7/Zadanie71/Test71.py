# Python 2.7.4.

import unittest
import fracs


class TestFracs(unittest.TestCase):

    def setUp(self):
        self.f12 = fracs.Frac(1,2)
        self.f12prim = fracs.Frac(1, 2)
        self.f13 = fracs.Frac(1,3)

    def test_str(self):
        self.assertEqual(str(fracs.Frac(2,1)), '2')
        self.assertEqual(str(fracs.Frac(1,2)), '1/2')

        # self.assertRaises(ValueError, fracs.Frac(2,0))

    def test_rep(self):
        self.assertEqual(repr(self.f12), 'Frac(1,2)')

    def test_cmp(self):
        self.assertEqual(cmp(self.f12, self.f12prim), 0)
        self.assertEqual(cmp(self.f12, self.f13), 1)
        self.assertEqual(cmp(self.f13, self.f12), -1)

    def test_add(self):
        self.assertEqual(1 + self.f12, fracs.Frac(3,2))
        self.assertEqual(self.f13 + 1, fracs.Frac(4,3))

    def test_sub(self):
        self.assertEqual(1 - self.f12, fracs.Frac(1,2))
        self.assertEqual(self.f12 - 1, fracs.Frac(-1,2))

    def test_pos(self):
        self.assertEqual(fracs.Frac(-1,-2).__pos__(), self.f12)
        self.assertEqual(fracs.Frac(-1,2).__pos__(), self.f12)
        self.assertEqual(fracs.Frac(1,-2).__pos__(), self.f12)




    def test_neg(self):
        self.assertEqual(fracs.Frac(-1,-2).__neg__(), fracs.Frac(-1,2))
        self.assertEqual(fracs.Frac(-1,2).__neg__(), fracs.Frac(1,2))
        self.assertEqual(fracs.Frac(1,-2).__neg__(), fracs.Frac(1,2))
        self.assertEqual(fracs.Frac(1,2).__neg__(), fracs.Frac(-1,2))

    def test_invert(self):
        self.assertEqual(self.f12.__invert__(), fracs.Frac(2,1))

    def test_float(self):
        self.assertEqual(self.f12.__float__(), 0.5)


    # def test_eq(self):
    #     self.assertTrue(self.C0 == self.C0prim)
    #     self.assertFalse(self.C0 == self.C112)

    def tearDown(self):
        pass
        # self.C0 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy