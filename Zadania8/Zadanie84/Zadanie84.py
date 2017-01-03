# Python 2.7.4.
import math
def heron(a, b, c):
    """Obliczanie pola powierzchni trojkata za pomoca wzoru
    Herona. Dlugosci bokow trojkata wynosza a, b, c."""
    p = 0.5 * (a + b + c)

    if a < b + c and  b < a + c and c < a + b:
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        raise ValueError('Podane wartosci nie tworza dlugosci bokow trojkata')

    return S
