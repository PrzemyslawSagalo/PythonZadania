import unittest
import Zadanie104

class TestCircles(unittest.TestCase):

    def setUp(self):
        self.testowy1 = Zadanie104.Queue(5)
        self.testowy2 = Zadanie104.Queue()

    def test_przepelnienie(self):
        '''
        test przepelnienia stosu
        '''
        with self.assertRaises(ValueError):
            for i in range(6):
                self.testowy1.put(i)

    def test_pobieranie_pusty(self):
        '''
        test pobierania z pustego stosu
        '''
        with self.assertRaises(ValueError):
            self.testowy2.get()



    def tearDown(self):
        self.testowy1 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy