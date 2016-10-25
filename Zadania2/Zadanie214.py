# Python 2.7.4

line = 'napis do testowania'
l_line = line.split()


l_line = sorted(l_line, key=len, reverse=True)

# Dlugosc najdluzszego wyrazu
dl_najdluzszego_wyrazu = len(l_line[0])

najdluzszy_wyraz = l_line[0]

print 'Nadzluzszy wyraz to: %s. A jego dlugosc wynosi %i.' % (najdluzszy_wyraz, dl_najdluzszego_wyrazu)
