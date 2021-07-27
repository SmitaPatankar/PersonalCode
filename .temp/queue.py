from collections import deque
q = deque()
q.append(1)  # push
q.append(2)  # push
q.append(3)  # push
print(q.popleft())  # pop
