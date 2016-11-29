# Python 2.7.4.

from Points import Point

class Circle:
    """Klasa reprezentujaca okregi na plaszczyznie."""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius
    #
    # def __repr__(self): pass       # "Circle(x, y, radius)"
    #
    # def __eq__(self, other):
    #     return self.pt == other.pt and self.radius == other.radius
    #
    # def __ne__(self, other):
    #     return not self == other
    #
    # def area(self): pass           # pole powierzchni
    #
    # def move(self, x, y): pass     # przesuniecie o (x, y)
    #
    # def cover(self, other): pass   # okrag pokrywajacy oba