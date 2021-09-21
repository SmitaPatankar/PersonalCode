# A function that takes a function as argument or returns a function as the result is a higher-order function.
#eg: map filter reduce sorted

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))
# ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']

def reverse(word):
     return word[::-1]
print(reverse('testing'))
# 'gnitset'
print(sorted(fruits, key=reverse))
# ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

# Modern Replacements for map, filter, and reduce
# A listcomp or a genexp does the job of map and filter combined, but is more readable.

#########################
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)

fact = factorial
#####################

print(list(map(fact, range(6))))
# [1, 1, 2, 6, 24, 120]
print([fact(n) for n in range(6)])
# [1, 1, 2, 6, 24, 120]
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
# [1, 6, 120]
print([factorial(n) for n in range(6) if n % 2])
# [1, 6, 120]

# gencomp is similar to map and filter as they return generators
# in python 2 list so listcomp

from functools import reduce
from operator import add
reduce(add, range(100))
# 4950
sum(range(100))  # better
# 4950

# all(iterable)  # if all are true
# any(iterable)

