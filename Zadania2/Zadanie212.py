# Python 2.7.4
line = 'napis do testowania'

split_line = line.split()

pierwsze_litery = ''
ostatnie_litery = ''

# for slowo in split_line:
# 	pierwsze_litery = pierwsze_litery + slowo[0]
# 	ostatnie_litery = ostatnie_litery + 

for slowo in split_line:
	pierwsze_litery += slowo[0]
	dl_slowo = len(slowo) - 1
	ostatnie_litery += slowo[dl_slowo]

print 'Napis z pierwszych liter wyrazow: %s' % pierwsze_litery
print 'Napis z ostatnich liter wyrazow: %s' % ostatnie_litery