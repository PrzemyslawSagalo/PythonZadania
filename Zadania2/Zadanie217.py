# Python 2.7.4

line = 'caac babac d abc'

line = line.split()

print 'Sortowanie wedlug kolejnosci alfabetycznej: ', sorted(line)
print 'Sortowanie wedlug dlugosci slowa: ', sorted(line, key=len, reverse=True)