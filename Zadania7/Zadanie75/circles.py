# Python 2.7.4

from Points import Point
import math
import numpy as np

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

        return 'Circle({0}, {1}, {2})'.format(x, y, radius)

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

    # def cover(self, other):
    #     """
    #     okrag pokrywajacy oba
    #     """
    #     x1 = self.pt.x
    #     y1 = self.pt.y
    #     r1 = self.radius
    #     x2 = other.pt.x
    #     y2 = other.pt.y
    #     r2 = other.radius
    #
    #     XX = np.array([[x1, 1],[x2, 1]])
    #     YY = np.array([y1, y2])
    #
    #     a, b = np.linalg.solve(XX, YY)
    #
    #     R = r2/2 + r1/2 + (math.sqrt(1 + pow(a,2))/2) * (x2-x1)
    #
    #     x = (2/math.sqrt(1+pow(a,2))) * (R - r2/2 - r1/2) + x1
    #     y = (2 * a/math.sqrt(1+pow(a,2))) * (R - r2/2 - r1/2) + y1
    #
    #     return Circle(x, y, R)

