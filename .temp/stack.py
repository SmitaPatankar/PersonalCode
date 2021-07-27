stack = []
stack.append(1)  # push
stack.append(2)  # push
stack.append(3)  # push
if stack:
    print(stack.pop())
else:
    print(None)
if stack:
    print(stack[-1])  # peek
else:
    print(None)
