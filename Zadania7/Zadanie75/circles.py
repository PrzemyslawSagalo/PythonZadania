# Python 2.7.4.

from Points import Point
import math

class Circle:
    """Klasa reprezentujaca okregi na plaszczyznie."""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        """
        Circle(x, y, radius)
        """
        x = self.pt.x
        y = self.pt.y
        radius = self.radius

        return "Circle({0}, {1}, {2})".format(x, y, radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        """
        pole powierzchni
        """
        val_area = math.pi * self.radius * self.radius
        return val_area

    def move(self, x_step, y_step):
        """
        przesuniecie o (x, y)
        """

        self.pt.x = self.pt.x + x_step
        self.pt.y = self.pt.y + y_step

    def cover(self, other):
        """
        okrag pokrywajacy oba
        """
        # x =

    # aself.assertRaises(ValueError, lambada: ~slef.zero)