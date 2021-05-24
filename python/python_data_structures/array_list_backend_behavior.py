# array sequences
# ---------------
# list, string, tuple
# support indexing
# 8 bits - 1 byte - slot with address
# python represents unicode characters with 2 bytes - 2 address slots
# stored and retrieved in O(1) - constant - when using indexing
# because address is already known

# list references
# ----------------
# one list indexes point to some elements in memory
# other list can also refer those
# array keeps some size, when full creates new one with more space, copies element, and older one becomes garbage

"""
import sys
n = 10
data = []
for i in range(10):
    a = len(data)
    b = sys.getsizeof(data)
    print(f"length: {a}, size: {b}")
    data.append(n)
# length: 0, size: 36
# length: 1, size: 52
# length: 2, size: 52
# length: 3, size: 52
# length: 4, size: 52
# length: 5, size: 68
# length: 6, size: 68
# length: 7, size: 68
# length: 8, size: 68
# length: 9, size: 100
"""
