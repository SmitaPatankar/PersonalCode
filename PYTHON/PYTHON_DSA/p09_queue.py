from collections import deque

print("creating queue(doubly ended queue)")
q = deque([0, 1, 2, 3])
print(q)

print("appending(pushing) elements")
q.append(4)
q.append(5)
q.append(6)
print(q)

print("popping element (from left)")
print(q.popleft())
print(q)
