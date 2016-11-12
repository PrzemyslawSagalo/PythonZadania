# Python 2.7.4

import unittest
from fracs import *

class TestFractions(unittest.TestCase):

	def setUp(self):
		self.zero = [0, 1]

	def test_add_frac(self):
		self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
		self.assertEqual(add_frac([1, 2], [1, 2]), [1, 1])

	def test_sub_frac(self):
		self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

	def test_mul_frac(self):
		self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

	def test_div_frac(self):
		self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

	def test_is_positive(self):
		self.assertEqual(is_positive([1,2]), 1)
		self.assertEqual(is_positive([-1,2]), 0)

	def test_is_zero(self):
		self.assertEqual(is_zero([0,2]), 1)
		self.assertEqual(is_zero([1,2]), 0)

	def test_cmp_frac(self):
		self.assertEqual(cmp_frac([1,1], [1,2]), 1)
		self.assertEqual(cmp_frac([1,2], [1,2]), 0)
		self.assertEqual(cmp_frac([1,2], [1,1]), -1)

	def test_frac2float(self):
		self.assertEqual(frac2float([1,2]), 0.5)

if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy
