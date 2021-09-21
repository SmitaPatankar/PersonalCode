def f_gen_1(name):
    for letter in name:
        yield letter

def f_1(func):
    for letter in func:
        pass
    for letter in func:
        yield letter

o1 = f_gen_1('smita')
o2=f_1(o1)
# print(next(o2))  # StopIteration

print('--------------1---------------------')

class F2:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        for letter in self.name:
            yield letter

def f2(func):
    for letter in func:
        pass
    for letter in func:
        yield letter

oo1 = F2('smita')
oo2=f2(oo1)
print(next(oo2))  # s

print('----------------2-------------------')

oo1 = f_gen_1('smita')
oo2=f2(oo1)
# print(next(oo2))  # StopIteration

print('----------------3-------------------')

class F3:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        for letter in self.name:
            yield letter

def f3_defensive(func):
    if iter(func) is iter(func):
        raise
    for letter in func:
        pass
    for letter in func:
        yield letter

oo1 = f_gen_1('smita')
oo2=f3_defensive(oo1)
# print(next(oo2))  # our error

print('----------------4-------------------')