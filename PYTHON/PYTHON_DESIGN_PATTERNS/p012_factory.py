# wholesale creation of object via separate class

from math import sin, cos


class Point:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}, {self.b}"

    class PointFactory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    p = Point(2, 3)
    p1 = Point.PointFactory.new_cartesian_point(2, 3)
    p2 = Point.PointFactory.new_polar_point(2, 3)
    print(p)
    print(p1)
    print(p2)
