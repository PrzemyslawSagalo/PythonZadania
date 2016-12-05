# Python 2.7.4

from fractions import gcd
class Frac:
    """Klasa reprezentujaca ulamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ValueError
        self.x = x
        self.y = y

    def __str__(self):
        """zwraca "x/y" lub "x" dla y=1"""
        if self.y == 1:
            frac_form = '{}'.format(self.x)
        else:
            frac_form = '{0}/{1}'.format(self.x, self.y)

        return frac_form

    def __repr__(self):
        """zwraca "Frac(x, y)"""

        return 'Frac({0},{1})'.format(self.x, self.y)

    def __cmp__(self, other):
        """porownywanie"""
        f1 = float(self.x) / self.y
        f2 = float(other.x) / other.y
        print f1, f2
        return cmp(f1, f2)

    def __add__(self, other):
        """frac1+frac2, frac+int"""
        if type(other) == float:
            other = other.as_integer_ratio()
            other = Frac(other[0], other[1])
        if type(other) == int:
            other = float(other)
            other = other.as_integer_ratio()
            other = Frac(other[0], other[1])
        result = [(self.x * other.y) + (self.y * other.x), self.y * other.y]
        val_GCD = gcd(*result)

        return Frac(result[0] / val_GCD, result[1] / val_GCD)

    __radd__ = __add__              # int+frac

    def __sub__(self, other):
        """frac1-frac2, frac-int"""
        if type(other) == float:
            other = other.as_integer_ratio()
            other = Frac(other[0], other[1])
        if type(other) == int:
            other = float(other)
            other = other.as_integer_ratio()
            other = Frac(other[0], other[1])
        result = [(self.x * other.y) - (self.y * other.x), self.y * other.y]
        val_GCD = gcd(*result)

        return Frac(result[0] / val_GCD, result[1] / val_GCD)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        """frac1*frac2, frac*int"""
        if type(other) == float or type(other) == int:
            other = Frac(float(other), 1)

        result = [self.x * other.x, self.y * other.y]
        val_GCD = gcd(*result)
        return Frac(result[0] / val_GCD, result[1] / val_GCD)

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):
        """frac1/frac2, frac/int"""
        if type(other) == float or type(other) == int:
            other = Frac(float(other), 1)

        result = [self.x * other.y, self.y * other.x]
        val_GCD = gcd(*result)

        return Frac(result[0] / val_GCD, result[1] / val_GCD)

    def __rdiv__(self, other):
        """int/frac"""
        if type(other) == float or type(other) == int:
            other = Frac(float(other), 1)

        result = [self.y * other.x, self.x * other.y]
        val_GCD = gcd(*result)

        return Frac(result[0] / val_GCD, result[1] / val_GCD)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        if self.x < 0 and self.y < 0:
            self.x = -1 * self.x
            self.y = -1 * self.y
        elif self.x >= 0 and self.y < 0:
            self.y = -1 * self.y
        elif self.x < 0 and self.y > 0:
            self.x = -1 * self.x

        return self

    def __neg__(self):
        """-frac = (-1)*frac"""
        if self.x < 0 and self.y < 0:
            val_frac = Frac(self.x, -1 * self.y)
        elif self.x >= 0 and self.y < 0:
            val_frac = Frac(self.x, -1 * self.y)
        elif self.x < 0 and self.y > 0:
            val_frac = Frac( -1 * self.x, self.y)
        elif self.x >= 0 and self.y >= 0:
            val_frac = Frac(-1 * self.x, self.y)

        return val_frac

    def __invert__(self):
        """odwrotnosc: ~frac"""
        return Frac(self.y, self.x)

    def __float__(self):
        """float(frac)"""
        return float(self.x) / self.y
