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
        max_x = max([abs(self.pt.x) + self.radius, abs(other.pt.x) + other.radius])
        max_y = max([max(abs(self.pt.y) + self.radius, abs(other.pt.y) + other.radius)])
        max_radius = max([max_x, max_y])

        return Circle(0, 0, max_radius)
