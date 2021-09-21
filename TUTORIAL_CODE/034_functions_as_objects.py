def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))
# 1405006117752879898543142606244511569936384000000000

print(factorial.__doc__)
# 'returns n!'

print(type(factorial))
# <class 'function'>

print(help(factorial))
'''
Help on function factorial in module __main__:

factorial(n)
    returns n!

None
'''

fact = factorial
print(fact)
# <function factorial at 0x...>
print(fact(5))
# 120
print(map(factorial, range(11)))
# <map object at 0x...>
print(list(map(fact, range(11))))
# [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

