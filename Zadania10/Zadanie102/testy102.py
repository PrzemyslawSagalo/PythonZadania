# Python 2.7.4

import unittest
import Zadanie102

class TestCircles(unittest.TestCase):

    def setUp(self):
        self.stos_testowy1 = Zadanie102.Stack()
        self.stos_testowy2 = Zadanie102.Stack()

    def test_przepelnienie(self):
        '''
        test przepelnienia stosu
        '''
        with self.assertRaises(ValueError):
            for i in range(11):
                self.stos_testowy1.push(i)

    def test_pobieranie_pusty(self):
        '''
        test pobierania z pustego stosu
        '''
        with self.assertRaises(ValueError):
            self.stos_testowy2.pop()


    def tearDown(self):
        self.stos_testowy1 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy