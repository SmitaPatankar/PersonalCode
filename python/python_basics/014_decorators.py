def addone(f):
    def addandaddone(a, b):
        return 1 + f(a, b)
    return addandaddone

@addone
def add(a, b):
    return a+b

print(add(1, 2))
