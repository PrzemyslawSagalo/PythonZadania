# Python 2.7.4.

def fibonacci(n):
    """Ciag Fibonacciego (definicja rekurencyjna)."""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

	return l_fib[n]


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