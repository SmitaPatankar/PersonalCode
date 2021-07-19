class Stack:
    # time = O(1)
    # space = O(1)
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)

    # time = O(1)
    # space = O(1)
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False

    # time = O(1)/O(n) or O(n^2) as some extra memory is allocated for list and when full it is moved in memory
    # space = O(1)
    def push(self, value):
        self.list.append(value)

    # time = O(1)
    # space = O(1)
    def pop(self):
        if self.isempty():
            return "nothing to pop"
        self.list.pop()        

    # time = O(1)
    # space = O(1)
    def peek(self):
        if self.isempty():
            return "nothing to peek"
        return self.list[-1]        

    # time = O(1)
    # space = O(1)
    def delete(self):
        self.list = None

s = Stack()
print(s.isempty())
s.push(0)
print(s)
s.pop()
s.pop()
print(s)
s.push(0)
s.push(1)
print("##########")
print(s)
print("##########")
print(s)
print("##########")
print(s)
print("##########")
print(s.peek())
s.delete()
