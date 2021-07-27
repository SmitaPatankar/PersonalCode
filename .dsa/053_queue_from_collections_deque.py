from collections import deque

q = deque(maxlen=3)
print(q)

q.append(0)
q.append(1)
q.append(2)
print(q)

q.append(3)
print(q)

q.popleft()
print(q)

q.clear()
print(q)
