# Python 2.7.4
import math
def heron(a, b, c):
    """Obliczanie pola powierzchni trojkata za pomoca wzoru
    Herona. Dlugosci bokow trojkata wynosza a, b, c."""
    if a + b < c:
        raise ValueError
    p = 0.5 * (a + b + c)
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return S
