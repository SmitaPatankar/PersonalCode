# binary search details
"""
elements should be in monotonic function i.e. increasing or decreasing order only
- take start, end, mid( (start+end)//2 )
- check mid
    - if key is same as mid, break
    - if key > mid, move start forward
    - if key < mid, move end backward
- do until start <= end
- search size keeps reducing by 2 each time
eg: 1000 -> 500 -> 250 -> 125 -> 62 -> 31 -> 15 -> 7 -> 3 -> 1
i.e. 10 comparisons for 1000 items
i.e. 1000/2^0 -> 1000/2^1 -> 1000/2^2......... -> 1000/2^?
i.e. 1000/2^? = 1
i.e. 2^? = 1000
i.e. ? = log 1000
i.e. O(logn) complexity
"""

# tbd: program: binary search - ROTI

# program: binary search
# logic: s+e/2 can go out of int range, (s + ((e-s)//2))
"""
even = [2,4,6,8,12,18]
odd = [3,8,11,14,16]
def binary_search(a, n):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = start + ((end-start)//2)
        if n < a[mid]:
            end = mid - 1
        elif n == a[mid]:
            return mid
        elif n > a[mid]:
            start = mid + 1
    return -1
print(binary_search(even, 4))
print(binary_search(odd, 14))
print(binary_search(even, 100))
print(binary_search(odd, 1))
"""
