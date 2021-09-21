# But inserting and removing from the left of a list (the 0-index end) is costly because the entire list must be shifted.

# The class collections.deque is a thread-safe double-ended queue designed for fast inserting and removing from both ends.

# deque can be bounded—i.e., created with a maximum length—and then, when it is full, it discards items from the opposite end when you append new ones.
# eg: last seen items

from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(3)
print(dq)
# deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
print(dq.rotate(-4))
print(dq)
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
dq.appendleft(-1)
print(dq)
# deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.extend([11, 22, 33])
print(dq)
# deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
dq.extendleft([10, 20, 30, 40])
print(dq)
# deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)

#  removing items from the middle of a deque is not as fast. It is really optimized for appending and popping from the ends.

'''
only list
s.__add__(s2)
s.__contains__(e)
s.copy()
s.index(e)
s.insert(p,e)
s.__mul__(n)
s.__imul__(n)
s.__rmul__(n)
s.sort([key], [reverse])

only deque
s.appendleft(e)
s.__copy__()
s.extendleft(i)
s.popleft()
s.rotate(n)

both
s.__iadd__(s2)
s.append(e)
s.clear()
s.count(e)
s.__delitem__(p)
s.extend(i)
s.__getitem__(p)
s.__iter__()
s.__len__()
s.pop() - pop(p) not in deque
s.remove(e)
s.reverse()
s.__reversed__()
s.__setitem__(p, e)

'''

'''
queue - they don’t discard items to make room as deque does.
multiprocessing - for interprocess communication. A specialized multiprocessing.JoinableQueue is also available for easier task management.
asyncio - but adapted for managing tasks in asynchronous programming
heapq - In contrast to the previous three modules, heapq does not implement a queue class, but provides functions like heappush and heappop that let you use a mutable sequence as a heap queue or priority queue.
'''