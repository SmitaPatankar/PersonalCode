"""
time = O(1)
space = O(1)
"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            if node.next == self.head:
                break
            node = node.next

    def create(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return "created"

csll = CSLL()
print(csll.create(0))
print([i for i in csll])
