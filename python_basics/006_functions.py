def myfunc(i):
    print(i)

print(myfunc)
# <function myfunc at 0x031C08E8>
myfunc(i=5)
# 5
myfunc(5)
# 5

def myfunc(i=2):
    print(i)

myfunc(5)
# 5
myfunc()
# 2

def sq(i):
    return i*2

print(sq(5))
# 10

def m(i):
    """
    This is a doc string.
    Can go multiple lines.
    """
    print(i)

print(help(m))
# Help on function m in module __main__:
#
# m(i)
#     This is a doc string.
#     Can go multiple lines.
#
# None
