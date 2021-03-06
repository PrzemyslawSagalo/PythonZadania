# Python 2.7.4.
import math

class Point:
    """Klasa reprezentujaca punkty na plaszczyznie."""

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        """
        zwraca string "(x, y)
        """
        return "({}, {})".format(self.x, self.y)


    def __repr__(self):
        """
        zwraca string "Point(x, y)"
        """
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        """
        obsluga point1 == point2
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        obsluga point1 != point2
        """
        return not self.__eq__(other)

    def __add__(self, other):
        """
        v1 + v2
        """
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        """
        v1 - v2
        """
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other):
        """
        v1 * v2, iloczyn skalarny
        """
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        """
        dlugosc wektora
        """
        return math.sqrt(self.__mul__(self))