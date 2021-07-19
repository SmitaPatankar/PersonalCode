class P:
    __x = 1
class C1(P):
    pass
class C2(P):
    pass

print(P.__x)  # AttributeError: type object 'P' has no attribute '__x'
print(C1.__x)
print(C2.__x)
