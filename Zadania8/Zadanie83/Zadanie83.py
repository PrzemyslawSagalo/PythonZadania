# Python 2.7.4
import math
import random

def calc_pi(n=100):
    """Obliczanie liczby pi metoda Monte Carlo.
    n oznacza liczbe losowanych punktow."""
    count = 0
    for i in xrange(n):

        x = random.random()
        y = random.random()

        if x*x + y*y <= 1:
            count += 1

    return (4 * count) / float(n)


# test
print 'Wartosc Pi z modulu math wynosi', math.pi
n = 10
print 'Pi dla {} iteracji MC wynosi'.format(n), calc_pi(n)
n = 1000
print 'Pi dla {} iteracji MC wynosi'.format(n), calc_pi(n)
n = 100000
print 'Pi dla {} iteracji MC wynosi'.format(n), calc_pi(n)
n = 10000000
print 'Pi dla {} iteracji MC wynosi'.format(n), calc_pi(n)
n = 100000000
print 'Pi dla {} iteracji MC wynosi'.format(n), calc_pi(n)

# ----------------------------------
# Wartosc Pi z modulu math wynosi 3.14159265359
# Pi dla 10 iteracji MC wynosi 2.8
# Pi dla 1000 iteracji MC wynosi 3.092
# Pi dla 100000 iteracji MC wynosi 3.14956
# Pi dla 10000000 iteracji MC wynosi 3.141916
# Pi dla 100000000 iteracji MC wynosi 3.141532