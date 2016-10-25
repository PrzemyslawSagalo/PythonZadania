# Python 2.7.4

liczba = 104050300

liczba = str(liczba)
l_liczba = list(liczba)

ilosc_zer = 0

for i in l_liczba:
	if i == '0':
		ilosc_zer += 1

print 'Ilosc zerw w liczbie %s to: %i.' % (liczba, ilosc_zer) 	