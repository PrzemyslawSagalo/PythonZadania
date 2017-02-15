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

    def cover(self, other):
        """
        okrag pokrywajacy oba
        """

        if other.pt.y < self.pt.y:
            x2 = float(self.pt.x)
            y2 = float(self.pt.y)
            r2 = float(self.radius)
            x1 = float(other.pt.x)
            y1 = float(other.pt.y)
            r1 = float(other.radius)
        else:
            x1 = float(self.pt.x)
            y1 = float(self.pt.y)
            r1 = float(self.radius)
            x2 = float(other.pt.x)
            y2 = float(other.pt.y)
            r2 = float(other.radius)

        D = math.sqrt(pow((x2-x1),2) + pow((y2 - y1),2)) # Odleglosc pomiedzy okregami

        if r1 >= r2:
            wiekszy = self
        else:
            wiekszy = other


        # Sprawdzamy czy jeden okrag zawiera sie w drugim.
        # Jezeli tak to zwracamy wiekszy okrag.
        if D < abs(r1 - r2):

            return wiekszy
        else:
            # Okregi leza na jednej prostej o rownaniu ogolnym y = ax + b.
            # Ponizej znajduja sie wspolczynniki tej prostej.
            try:
                a = (y2 - y1) / (x2 - x1)
                b = (y1 * x2 - y2 * x1) / (x2 - x1)
            except ZeroDivisionError:
                a = 0
                b = 0

            R = (1/2.) * (r1 + r2 + D)

            L1 = pow((R-r2),2)
            L2 = pow((R-r1),2)

            try:
                x = (L1 - L2 - pow(x2,2) + pow(x1,2) - pow(y2,2) + pow(y1,2) - 2 * b * (y1 - y2)) / (2 * ( (x1 - x2) +  (y1 - y2) * a))
                y = a * x + b
            except ZeroDivisionError:
                R = (r2 + r1 + y2 - y1) / 2.0
                x = x1
                y = (R - r1) + y1

            return Circle(x, y, R)

