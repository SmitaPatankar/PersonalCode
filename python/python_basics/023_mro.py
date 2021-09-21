"""
method resolution order

----------

python2
deep left right - DLR
remove duplicates from end

order doesn't make sense

we can inherit from Object explicitly for python3 like behavior

----------

python3
linearization = MRO
in merge, head means first item of element and rest all are tail
if head is not present in an other tail, take it out from everywhere and start over
else just move forward to next element and repeat the same until you reach end

order makes sense else fails

inherits from object by default

class D: pass
class E: pass
class F: pass
class B(D, E): pass
class C(D, F): pass
class A(B, C): pass

1. L[D] = DO
2. L[E] = EO
3. L[F] = FO

4.
L[B] = B + merge(L[D] + L[E] + DE)
L[B] = B + merge(DO, EO,DE)
L[B] = BD + merge(O,EO,E)
L[B] = BDE + merge(O,O)
L[B] = BDEO

5.
L[C] = C + merge(L[D] + L[F] + DF)
L[C] = C + merge(DO, FO, DF)
L[C] = CD + merge(O,FO,F)
L[C] = CDF + merge(O,O)
L[C] = CDFO

6.
L[A] = A + merge(L[B] + L[C] + BC)
L[A] = A + merge(BDEO + CDFO + BC)
L[A] = AB + merge(DEO + CDFO + C)
L[A] = ABC + merge(DEO + DFO)
L[A] = ABCD + merge(EO + FO)
L[A] = ABCDE + merge(O + FO)
L[A] = ABCDEF + merge(O + O)
L[A] = ABCDEFO
"""


class A: pass  # A
class B: pass  # B
class C(A, B): pass  # CAB
class D(B, A): pass  # DBA
# class X(C, D): pass

# python2
# XCABD

# python3
# L[X] = X + merge(L[C], L[D], CD)
# L[X] = X + merge(CAB, DBA, CD)
# L[X] = X + C + merge(AB, DBA, D)
# L[X] = X + C + D + merge(AB, BA)
# L[X] = X + C + D + merge(AB, BA)  # issue


print(D.mro())
