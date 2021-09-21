import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

# Shortcut to bingo.pick(): bingo()

bingo = BingoCage(range(3))
bingo.pick()
# 1
bingo()
# 0
print(callable(bingo))
# True

# A class implementing __call__ is an easy way to create function-like objects that have some internal state that must be kept across invocations

# Decorators must be functions, but it is sometimes convenient to be able to “remember” something between calls of the decorator
# closures

