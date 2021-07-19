class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LL:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curnode = self.head
        while curnode:
            yield curnode.value
            curnode = curnode.next

class Stack:
    # time = O(1)
    # space = O(1)
    def __init__(self):
        self.ll = LL()

    # time = O(1)
    # space = O(1)
    def isempty(self):
        return True if not self.ll.head else False

    # time = O(1)
    # space = O(1)
    def push(self, value):
        node = Node(value)
        node.next = self.ll.head
        self.ll.head = node

    # time = O(1)
    # space = O(1)
    def pop(self):
        if self.isempty():
            return "nothing to pop"
        nodevalue = self.ll.head.value
        self.ll.head = self.ll.head.next
        return nodevalue

    # time = O(1)
    # space = O(1)
    def peek(self):
        if self.isempty():
            return "nothing to peek"
        return self.ll.head.value

    def __str__(self):
        values = [str(x) for x in self.ll]
        return "\n".join(values)

    # time = O(1)
    # space = O(1)
    def delete(self):
        self.ll.head = None

s = Stack()
print(s.isempty())
print(s.push(5))
print(s.push(6))
print(s.push(7))
print("------------")
print(s)
print("------------")
print(s.pop())
print("------------")
print(s)
print("------------")
print(s.peek())
s.delete()
print(s)
