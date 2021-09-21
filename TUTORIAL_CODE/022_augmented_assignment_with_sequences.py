# The special method that makes += work is __iadd__ (for “in-place addition”).
# However, if __iadd__ is not implemented, Python falls back to calling __add__

# a += b

l = [1, 2, 3]
print(id(l))
# 4311953800
l *= 2
print(l)
# [1, 2, 3, 1, 2, 3]
print(id(l))
# 4311953800

t = (1, 2, 3)
print(id(t))
# 4312681568
t *= 2
print(id(t))
# 4301348296

print("###########")

t = (1, 2, [30, 40])
# t[2] += [50, 60]
# print(t)
# TypeError: 'tuple' object does not support item assignment

# byte code
import dis
dis.dis('s[a] += b')
'''
 1           0 LOAD_NAME                0 (s)
              2 LOAD_NAME                1 (a)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR
              8 LOAD_NAME                2 (b)
             10 INPLACE_ADD
             12 ROT_THREE
             14 STORE_SUBSCR
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE
'''

# Putting mutable items in tuples is not a good idea.

