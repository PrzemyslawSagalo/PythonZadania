import Points

point0 = Points.Point(0, 0)
point1 = Points.Point(1, 1)
point1bis = Points.Point(1, 1)
point2 = Points.Point(1, 2)

print point1.__str__()
print point1.__repr__()
print point1.__eq__(point0)
print point1.__eq__(point1bis)