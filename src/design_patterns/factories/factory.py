# Factory pattern
# A component responsible solely for the wholesale (not piecewise) creation of objects.
from math import sin, cos
from abc import ABC, abstractmethod


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    class PointFactory:
        def new_cartesian_point(self, x, y):
            p = Point()
            p.x = x
            p.y = y
            return p

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))
    # singleton factory
    factory = PointFactory()


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)
    p3 = Point.factory.new_cartesian_point(2, 3)
    print(p.x)
    print(p.y)
    print(p2.x)
    print(p2.y)
    print(p3.x)
    print(p3.y)
