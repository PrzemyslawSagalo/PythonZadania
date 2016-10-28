# Python 2.7.4

# f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2)

def rek_fibonacci(n):
    """Ciag Fibonacciego (definicja rekurencyjna)."""
    if n == 0 or n == 1:
        return n
    else:
        return rek_fibonacci(n-1) + rek_fibonacci(n-2)

def iter_fibonacci(n):
	"""Ciag Fibonacciego (definicja iteracyjna)."""
	l_fib = [0, 1]

	i = 2

	while i <= n:
		val_i_fib = l_fib[i-1] + l_fib[i-2]
		l_fib.append(val_i_fib)
		i += 1

	return l_fib[n]

# -----------------------------------
# test
test_val = 23
if rek_fibonacci(test_val) == iter_fibonacci(test_val):
	print 'OK.'