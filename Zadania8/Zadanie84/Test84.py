# Python 2.7.4

import unittest
import Zadanie84
import math

class TestCircles(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple(self):      # test punktow i promienia
        self.assertAlmostEquals(Zadanie84.heron(math.sqrt(2), 1, 1), 0.5)

        with self.assertRaises(ValueError):
            Zadanie84.heron(-1, 1, 1)

if __name__ == "__main__":
    unittest.main()     # wszystkie testy