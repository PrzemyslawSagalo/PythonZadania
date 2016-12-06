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
print calc_pi(100000000)
print math.pi