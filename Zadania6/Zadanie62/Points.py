# Python 2.7.4

class Point:
    """Klasa reprezentujaca punkty na plaszczyznie."""

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): pass         # zwraca string "(x, y)"

    def __repr__(self): pass        # zwraca string "Point(x, y)"

    def __eq__(self, other): pass   # obsluga point1 == point2

    def __ne__(self, other):        # obsluga point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): pass  # v1 + v2

    def __sub__(self, other): pass  # v1 - v2

    def __mul__(self, other): pass  # v1 * v2, iloczyn skalarny

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self): pass          # dlugosc wektora