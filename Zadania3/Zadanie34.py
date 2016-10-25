# Python 2.7.4

while 1:
	x = raw_input('Wpisz liczbe: \n')
	if x == 'stop':
		break
	else:
		try:
			x = float(x)
			print x, x ** 3
		except ValueError:
			print 'Blad! To nie jest liczba!'