# FIFO
# push
# pop

from collections import deque

print("create")
q = deque()
print(q)

print("push")
q.append(0)
print(q)

print("push")
q.append(1)
print(q)

print("pop")
print(q.popleft())
print(q)
