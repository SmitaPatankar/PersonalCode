from abc import ABC, abstractmethod
from enum import Enum


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("drinking tea")


class Coffee(HotDrink):
    def consume(self):
        print("drinking coffee")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"using tea bag - {amount}")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"using coffee powder - {amount}")
        return Coffee()


def make_drink(type):
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(50)


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = 1
        TEA = 2

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((factory_name, factory_instance))

    def make_drink(self):
        print("Available drinks:")
        for f in self.factories:
            print(f[0])
        s = input(f"please pick drink: 0-{len(self.factories) - 1}")
        idx = int(s)
        s = input("amount?")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    h = HotDrinkMachine()
    h.make_drink()
