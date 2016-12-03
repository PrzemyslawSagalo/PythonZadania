class Frac:
    """Klasa reprezentujaca ulamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        self.x = x
        self.y = y

    def __str__(self): pass         # zwraca "x/y" lub "x" dla y=1

    def __repr__(self): pass        # zwraca "Frac(x, y)"

    def __cmp__(self, other): pass  # porownywanie

    def __add__(self, other): pass  # frac1+frac2, frac+int

    __radd__ = __add__              # int+frac

    def __sub__(self, other): pass  # frac1-frac2, frac-int

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other): pass  # frac1*frac2, frac*int

    __rmul__ = __mul__              # int*frac

    def __div__(self, other): pass  # frac1/frac2, frac/int

    def __rdiv__(self, other): pass # int/frac

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self): pass         # -frac = (-1)*frac

    def __invert__(self): pass      # odwrotnosc: ~frac

    def __float__(self): pass       # float(frac)

