from singleton_base import Tigger

a = Tigger()
b = Tigger()

print(id(a) == id(b))
