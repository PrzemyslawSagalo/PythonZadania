# Python 2.7.4

import unittest
import Zadanie81
import math

class TestCircles(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple(self):      # test punktow i promienia
        self.assertEquals(Zadanie81.solve1(0,1,0), 'y=0')
        self.assertEquals(Zadanie81.solve1(0,1,2), 'y=-2.0')
        self.assertEquals(Zadanie81.solve1(1,1,0), 'y=-1.0*x')
        self.assertEquals(Zadanie81.solve1(1,1,2), 'y=-1.0*x-2.0')


        with self.assertRaises(ValueError):
            Zadanie81.solve1(1,0,1)

if __name__ == "__main__":
    unittest.main()     # wszystkie testy