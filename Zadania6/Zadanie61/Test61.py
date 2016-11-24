import unittest
import Zadanie61

class TestTime(unittest.TestCase):

    def setUp(self):
        self.Time1s = Zadanie61.Time(1)
        self.Time1s_bis = Zadanie61.Time(1)
        self.Time1h = Zadanie61.Time(3600)

    def test_print(self):      # test str() i repr()
        self.assertEqual(self.Time1s.__str__(), '00:00:01')
        self.assertEqual(self.Time1h.__str__(), '01:00:00')

        self.assertEqual(self.Time1s.__repr__(), 'Time(1)')
        self.assertEqual(self.Time1h.__repr__(), 'Time(3600)')

    def test_add(self):
        self.assertEqual(self.Time1h + self.Time1s, Zadanie61.Time(3601))

    def test_cmp(self):
        self.assertEqual(self.Time1s.__cmp__(self.Time1s_bis), 0)
        self.assertEqual(self.Time1h.__cmp__(self.Time1s), 1)
        self.assertEqual(self.Time1s.__cmp__(self.Time1h), -1)

    def test_int(self):
        self.assertEqual(self.Time1h.__int__(), 3600)

    def tearDown(self):
        self.Time1s = None
        self.Time1h = None
        self.Time1s_bis = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy