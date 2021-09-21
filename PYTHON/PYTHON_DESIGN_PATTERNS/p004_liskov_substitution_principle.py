class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"width - {self.width}, height - {self.height}"


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


# interface that works on base class should also work on derived class
# violated
def use_it(r):
    w = r.width
    r.height = 10
    expected_area = w*10
    actual_area = r.area
    print(f"expected area: {expected_area}, actual area: {actual_area}")


r = Rectangle(2, 3)
use_it(r)

s = Square(5)
use_it(s)
