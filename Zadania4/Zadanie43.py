# Python 2.7.4

import math

def Mfactorial(n):
	val_factorial = 1
	if n > 1:
		i = 2
		while i <= n:
			val_factorial *= i
			i += 1
	elif n <= 1:
		val_factorial = 1
	
	return val_factorial 

# Only to check
# for i in xrange(10):
# 	if Mfactorial(i) == math.factorial(i):
# 		print i, 'OK'