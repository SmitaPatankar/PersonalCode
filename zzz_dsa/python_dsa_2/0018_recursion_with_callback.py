"""
somerecursive takes array and callback for isodd
somerecursive returns true if single value in array returns true when passed to callback
somerecursive returns false otherwise
"""

def isodd(n):
    print(f"checking {n}")
    return n%2 != 0

def rec(arr, f):
    if len(arr) == 0:
        return False
    if not f(arr[0]):
        return rec(arr[1:], f)
    return True

print(rec([4,2,3,1,8], isodd))
print(rec([2,4], isodd))
print(rec([1], isodd))
print(rec([], isodd))
