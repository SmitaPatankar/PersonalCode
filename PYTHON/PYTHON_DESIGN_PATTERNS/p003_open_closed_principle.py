# learn more
# __and__

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# open for extension, closed for modification
class Specification:
    def is_satisfied(self, product):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, products, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, product):
        return product.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, product):
        return product.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, product):
        print(f"args: {self.args}")
        print(f"result: {str(all(map(lambda spec: spec.is_satisfied(product), self.args)))}")
        return all(map(lambda spec: spec.is_satisfied(product), self.args))


class BetterFilter(Filter):
    def filter(self, products, spec):
        for product in products:
            if spec.is_satisfied(product):
                yield product


if __name__ == "__main__":
    apple = Product("apple", Color.GREEN, Size.SMALL)
    tree = Product("tree", Color.GREEN, Size.LARGE)
    house = Product("house", Color.GREEN, Size.LARGE)

    products = [house]

    bf = BetterFilter()

    print("Green products:")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name}")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name}")

    print("Large green products:")
    large_green = large & green & large
    for p in bf.filter(products, large_green):
        print(f" - {p.name}")
