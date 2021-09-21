from cProfile import Profile
from pstats import Stats
x
def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result


# def insert_value(array, value):
#     for i, existing in enumerate(array):
#         if existing > value:
#             array.insert(i, value)
#             return
#     array.append(value)

from random import randint

max_size = 10**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

# cProfile better than profile as the latter puts load on program
# profile actual code and not external factors like network connection

# profiler = Profile()
# profiler.runcall(test)
#
# stats = Stats(profiler)
# stats.strip_dirs()
# stats.sort_stats('cumulative')
# stats.print_stats()

'''
>>>
         20003 function calls in 1.812 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.812    1.812 main.py:34(<lambda>)
        1    0.003    0.003    1.812    1.812 main.py:10(insertion_sort)
    10000    1.797    0.000    1.810    0.000 main.py:20(insert_value)
     9992    0.013    0.000    0.013    0.000 {method 'insert' of 'list' objects}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

from bisect import bisect_left

def insert_value(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)

profiler = Profile()
profiler.runcall(test)

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()

'''
>>>
         30003 function calls in 0.028 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.028    0.028 main.py:34(<lambda>)
        1    0.002    0.002    0.028    0.028 main.py:10(insertion_sort)
    10000    0.005    0.000    0.026    0.000 main.py:112(insert_value)
    10000    0.014    0.000    0.014    0.000 {method 'insert' of 'list' objects}
    10000    0.007    0.000    0.007    0.000 {built-in method bisect_left}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

def my_utility(a, b):
    # ...

def first_func():
    for _ in range(1000):
        my_utility(4, 5)

def second_func():
    for _ in range(10):
        my_utility(1, 3)

def my_program():
    for _ in range(20):
        first_func()
        second_func()

'''
>>>
         20242 function calls in 0.208 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.208    0.208 main.py:176(my_program)
       20    0.005    0.000    0.206    0.010 main.py:168(first_func)
    20200    0.203    0.000    0.203    0.000 main.py:161(my_utility)
       20    0.000    0.000    0.002    0.000 main.py:172(second_func)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

stats.print_callers()

'''
>>>
   Ordered by: cumulative time

Function                               was called by...
                                           ncalls    tottime  cumtime
main.py:176(my_program)                <-
main.py:168(first_func)                <-      20     0.005    0.206  main.py:176(my_program)
main.py:161(my_utility)                <-   20000     0.202    0.202  main.py:168(first_func)
                                              200     0.002    0.002  main.py:172(second_func)
main.py:172(second_func)               <-      20     0.000    0.002  main.py:176(my_program)
'''

