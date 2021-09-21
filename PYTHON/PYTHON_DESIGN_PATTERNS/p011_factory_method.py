# wholesale creation of object via method

from math import sin, cos


class Point:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    @classmethod
    def new_cartesian_point(cls, x, y):
        return cls(x, y)

    @classmethod
    def new_polar_point(cls, rho, theta):
        return cls(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f"{self.a}, {self.b}"


if __name__ == "__main__":
    p = Point(2, 3)
    p1 = Point.new_cartesian_point(2, 3)
    p2 = Point.new_polar_point(2, 3)
    print(p)
    print(p1)
    print(p2)
