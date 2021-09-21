class Stack:
    # time = O(1)
    # space = O(1)
    def __init__(self, maxsize):
        self.maxsize = maxsize
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

    # time = O(1)
    # space = O(1)
    def isfull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False

    # time = O(1)/O(n^2) as some extra memory is allocated for list and when full it is moved in memory
    # space = O(1)
    def push(self, value):
        if self.isfull():
            return "no space"
        self.list.append(value)
        return "pushed"

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

s = Stack(5)
print(s.isempty())
print(s.isfull())
print(s.push(0))
print(s.push(1))
print(s.push(2))
print(s)
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s.isfull())
print(s.peek())
s.delete()