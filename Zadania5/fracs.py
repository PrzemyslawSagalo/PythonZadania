# Python 2.7.4

def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

def add_frac(frac1, frac2):
	"""
	 frac1 + frac2
	"""
	if frac1[1] == 0 or frac2[1] == 0:
		raise ZeroDivisionError
	else:
		result = [(frac1[0]*frac2[1]) + (frac1[1]*frac2[0]), frac1[1]*frac2[1]]
		val_GCD = GCD(*result)
		result = [result[0]/val_GCD, result[1]/val_GCD]

	return result

def sub_frac(frac1, frac2):
	"""
	 frac1 - frac2
	"""
	if frac1[1] == 0 or frac2[1] == 0:
		raise ZeroDivisionError
	else:
		result = [(frac1[0]*frac2[1]) - (frac1[1]*frac2[0]), frac1[1]*frac2[1]]
		val_GCD = GCD(*result)
		result = [result[0]/val_GCD, result[1]/val_GCD]

	return result

def mul_frac(frac1, frac2):
	"""
	 frac1 * frac2
	"""
	if frac1[1] == 0 or frac2[1] == 0:
		raise ZeroDivisionError
	else:
		result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
		val_GCD = GCD(*result)
		result = [result[0]/val_GCD, result[1]/val_GCD]

	return result

def div_frac(frac1, frac2):
	"""
	 frac1 / frac2
	"""
	if frac1[1] == 0 or frac2[1] == 0:
		raise ZeroDivisionError
	else:
		result = [frac1[0] * frac2[1], frac1[1] * frac2[0]]
		val_GCD = GCD(*result)
		result = [result[0]/val_GCD, result[1]/val_GCD]

	return result

def is_positive(frac):
	"""
	bool, czy dodatni
	"""
	is_positive = 0

	if frac[1] == 0:
		raise ZeroDivisionError
	else:
		if frac[0] >= 0 and frac[1] > 0:
			is_positive = 1

	return is_positive 


def is_zero(frac):
	"""
	bool, typu [0, x]
	"""
	is_num_eq_zero = 0

	if frac[1] == 0:
		raise ZeroDivisionError
	else:
		if frac[0] == 0:
			is_num_eq_zero = 1

	return is_num_eq_zero

def cmp_frac(frac1, frac2):
	"""
	-1 | 0 | +1
	"""
	which_greater = 0

	if frac1[1] == 0 or frac2[1] == 0:
		raise ZeroDivisionError
	else:
		frac1 = frac1[0] / frac1[1]
		frac2 = frac2[0] / frac2[1]

		if 	frac1 > frac2:
			which_greater = 1
		elif frac1 == frac2:
			which_greater = 0
		elif frac1 < frac2:
			which_greater = -1

	return which_greater

def frac2float(frac):
	"""
	conversion to float
	"""

	if frac[1] == 0:
		raise ZeroDivisionError
	else:
		result = float(frac[0]) / float(frac[1])

	return result
