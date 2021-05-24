# hardware dependent profiling
##############################

"""
def sum1(n):
    res = 0
    for i in range(n+1):
        res = res + i
    return res


sum1(5)


def sum2(n):
    return (n*(n+1))/2


sum2(5)

from timeit import timeit

print(timeit("sum1(100)","from __main__ import sum1"))  # 16.844282
print(timeit("sum2(100)","from __main__ import sum2"))  # 0.6007200000000026
"""

# hardware independent profiling - Big O
########################################

# objectively compares the number of assignments each algorithm makes
# checks how time will grow when input gets large
# identifies the limiting factor of algorithm
# O(1) or O(log(n)) is good
# O(n) is fair
# O(nlogn) is bad
# O(n^2), O(2^n), O(n!) are horrible

# time - O(1) - constant
# ----------------------
"""
def func_constant(values):
    print(values[0])


func_constant([1, 2, 3])
"""

# time - O(n) - linear
# ---------------------
"""
def func_lin(lst):
    for val in lst:
        print(val)


func_lin([1, 2, 3])
"""

# time - O(n^2) - quadratic
# -------------------------
"""
def func_quad(lst):
    for item1 in lst:
        for item2 in lst:
            print(item1, item2)


lst = [1, 2, 3]
func_quad(lst)
"""

# space - O(1) - constant
# -----------------------
"""
def memory(n=10):
    for x in range(n):
        print("something")


memory(10)
"""
