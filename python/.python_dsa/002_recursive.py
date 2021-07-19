# notes

# apply same solution on different inputs
# solution of problem depends on solution of smaller instance of same problem
# stop at smallest instance

# trees, graphs, greedy algorithms, dynamic programming algorithms use recursion

# uses stack memory to store functions and executes them in LIFO order (last function is not stored as it is directly called)
# stack uses push and pop

# python has limitations of approx 1000 recursive methods in memory after which it throws error
# can be modified

# ############################################################################

# modify recursive limit code
import sys
sys.setrecursionlimit(10000)

# ############################################################################

# generic code
# call itself
# exit from loop
# constraints
"""
def recursionmethod(parameters):
    if exitfromconditionsatisified:
        return somevalue
    recursionmethod(modifiedparameters)
"""

# ############################################################################

# examples code

"""
def openrussiandoll(doll):
    if doll == 1:
        print("all dolls are opened")
    openrussiandoll(doll-1)
"""

def sum(a, n):
    if n == 1:
        return a[0]
    return sum(a, n-1) + a[n-1]
print(sum([10,20,30], 3))

def recursivemethod(n):
    if n<1:
        print("n<1")
    else:
        recursivemethod(n-1)
recursivemethod(5)

def factorial(n):
    assert n >= 0 and int(n) == n, "number must be +ve int only"
    if n in [0,1]:
        return 1
    return factorial(n-1) * n
print(factorial(5))

def fib(n):
    assert n >= 0 and int(n) == n, "number must be +ve int only"
    if n in [0,1]:
        return n
    return fib(n-1) + fib(n-2)
print(fib(4))

# divide by 10 to get digits of number as remainder and rest of the digits as quotient
def sumofdigits(n):
    assert n>=0 and int(n) == n, "number must be +ve int only"
    if n == 0:
        return 0
    return sumofdigits(n//10) + n % 10
print(sumofdigits(125))

def pow(base, exp):
    assert exp>=0 and int(exp) == exp, "exp must be +ve int only"
    if exp == 0:
        return 1
    return base * pow(base, exp-1)
print(pow(3,4))

# 48, 18
# 48 = 2 * 2 * 2 * 2 * 3
# 18 = 2 * 3 * 3
# product of common numbers = 2 * 3 = 6
# OR---------------------------------------->
# euclidean algorithm (used here)
# 48, 18
# 48/18 = 2, 48 % 18 = 12
# 18/12 = 1, 18 % 12 = 6
# 12/6 = 2, 12 % 6 = 0
def gcd(a, b):
    assert int(a) == a and int(b) == b, "numbers must be int"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    return gcd(b, a%b)
print(gcd(48,18))

# 13
# 13/2=6 13%2=1
# 6/2=3  6%2=0
# 3/2=1  3%2=1
# 1/2=0  1%2=1
# stop as quotient became 0
# multiply 10 to each digit from bottom and then add upper digit to join them
# 1101
def dec_to_bin(n):
    assert int(n) == n, "must be int"
    if n == 0:
        return 0
    return dec_to_bin(int(n/2))*10 + (n%2)
print(dec_to_bin(13))
