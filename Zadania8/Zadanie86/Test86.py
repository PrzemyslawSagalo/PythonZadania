# Python 2.7.4

import unittest
import Zadanie86
import math

class TestCircles(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple(self):      # test punktow i promienia
        self.assertEquals(Zadanie86.dyn_P(0,0),Zadanie86.rek_P(0,0))
        self.assertEquals(Zadanie86.dyn_P(10, 8), Zadanie86.rek_P(10, 8))

        with self.assertRaises(ValueError):
            Zadanie86.dyn_P(-1,0)
        with self.assertRaises(ValueError):
            Zadanie86.dyn_P(-1,0)


if __name__ == "__main__":
    unittest.main()     # wszystkie testy