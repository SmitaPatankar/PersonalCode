"""
each node refers to both previous and next node
create head as null
create tail as null
create node with value and with prev and next as null
point head to node
point tail to node

time = O(1)
space = O(1)
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def create(self, nodevalue):
        node = Node(nodevalue)
        self.head = node
        self.tail = node
        return("created")

dll = DLL()
print(dll.create(0))
print([i for i in dll])
