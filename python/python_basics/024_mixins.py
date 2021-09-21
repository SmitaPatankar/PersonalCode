# mixin
# provide many optional features to one class
# provide one feature to multiple classes

# locked
class A: total = 500
class B(A): pass
class C(A): pass


# ours
class M:
    def print_total(self):
        print(self.total)
class D(B, M): pass
class E(C, M): pass


d = D()
d.print_total()
