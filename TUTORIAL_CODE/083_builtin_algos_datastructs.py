from collections import deque

fifo = deque()
fifo.append(1)      # Producer
x = fifo.popleft()  # Consumer

# But inserting or removing items from the head of a list takes linear time, which is much slower than the constant time of a deque.

a = {}
a['foo'] = 1
a['bar'] = 2

from random import randint
# Randomly populate 'b' to cause hash conflicts
while True:
    z = randint(99, 1013)
    b = {}
    for i in range(z):
        b[i] = i
    b['foo'] = 1
    b['bar'] = 2
    for i in range(z):
        del b[i]
    if str(b) != str(a):
        break

print(a)
print(b)
print('Equal?', a == b)

# {'foo': 1, 'bar': 2}
# {'bar': 2, 'foo': 1}
# Equal? True

from collections import OrderedDict

a = OrderedDict()
a['foo'] = 1
a['bar'] = 2
b = OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'

for value1, value2 in zip(a.values(), b.values()):
    print(value1, value2)

# 1 red
# 2 blue

stats = {}
key = 'my_counter'
if key not in stats:
   stats[key] = 0
stats[key] += 1

# The defaultdict class from the collections module simplifies this by automatically storing a default value when a key doesn’t exist.

from collections import defaultdict
stats = defaultdict(int)
stats['my_counter'] += 1

'''
Heaps are useful data structures for maintaining a priority queue. The heapq module provides functions for creating heaps in standard list types with functions like heappush, heappop, and nsmallest.
Items of any priority can be inserted into the heap in any order.
'''

from heapq import heappush, heappop, nsmallest
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)

# Items are always removed by highest priority (lowest number) first.

print(heappop(a), heappop(a), heappop(a), heappop(a))
# 3 4 5 7

# The resulting list is easy to use outside of heapq. Accessing the 0 index of the heap will always return the smallest item.

a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
assert a[0] == nsmallest(1, a)[0] == 3

print('Before:', a)
a.sort()
print('After: ', a)

# Before: [3, 4, 7, 5]
# After:  [3, 4, 5, 7]

'''
Searching for an item in a list takes linear time proportional to its length when you call the index method.
'''

x = list(range(10**6))
i = x.index(991234)

# The bisect module’s functions, such as bisect_left, provide an efficient binary search through a sequence of sorted items. The index it returns is the insertion point of the value into the sequence.

