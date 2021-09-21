from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ""


class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has color {self.color}"


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape} has {self.transparency*100}% transparency"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"circle with radius {self.radius}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def resize(self, side):
        self.side *= side

    def __str__(self):
        return f"square with side {self.side}"


if __name__ == "__main__":
    c = Circle(2)
    print(c)

    cs = ColoredShape(c, "red")
    print(cs)

    cts = TransparentShape(cs, 0.5)
    print(cts)
