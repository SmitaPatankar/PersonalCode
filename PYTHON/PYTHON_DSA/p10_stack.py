print("creating stack (list)")
stack = [1, 2, 3]
print(stack)

print("pushing(appending) elements")
stack.append(4)
stack.append(5)
stack.append(6)
print(stack)

print("popping element (by default from right)")
stack.pop()
print(stack)

print("peeking element (getting element at last index)")
print(stack[-1])

print("clearing stack")
stack.clear()
print(stack)
