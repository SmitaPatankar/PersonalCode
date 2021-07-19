class C:
    def __init__(self):
        self.m = 0

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, value):
        if value < 10:
            self._m = value
        else:
            raise ValueError

c = C()
print(c.m)
# c.m = 100
# print(c.m)
c.m=5
print(c.m)
