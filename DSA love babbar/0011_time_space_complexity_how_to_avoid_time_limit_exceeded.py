# time complexity
"""
- time taken by algo as per length if input
"""

# complexity types
"""
big o - worst case
omega - best case
theta - average case
"""

# complexities from least to highest
# ignore lower degree
# ignore constant
# nested loops = *
# separate loops = +
"""
O(1) - constant - eg: print hello 11 times
O(log n) - logarithmic time - eg: binary search
O(n) - linear - eg: print hello n times
O(nlogn)
O(n^2) - quadratic time - eg: 2 nested loops
O(n^3) - cubic time - eg: 3 nested loops
O(2^n)
O(n!)
"""

# how much complexity is ideal to avoid time limit exceeded error
"""
nowadays machines have capacity to run 10**8 operations per second
refer program constraints to decide
eg: if input is till 10**4, we can use max O(n*2) complexity not more than that to finish in one sec
"""

# space complexity
"""
- memory taken as per length of input given to algo
- making variables like int, array of fixed size is constant space O(1)
- making variable like array and dynamically putting n elements to it is linear O(n)
- even if array is created from scratch again and again with n elements, it is O(n) at a time
"""