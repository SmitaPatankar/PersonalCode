"""
create blank head referring to null
create blank tail referring to null
create node with null value and reference to null
refer head to node
refer tail to node

time = O(1)
space = O(1)
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

singlylinkedlist = SLinkedList()
node1 = Node(1)
node2 = Node(2)
singlylinkedlist.head = node1
node1.next = node2
singlylinkedlist.tail = node2
