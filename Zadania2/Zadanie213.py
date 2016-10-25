# Python 2.7.4
line = 'napis test'

lacza_dlugosc_wyrazow = 0

line = line.split()

for wyraz in line:
	lacza_dlugosc_wyrazow += len(wyraz)

print lacza_dlugosc_wyrazow