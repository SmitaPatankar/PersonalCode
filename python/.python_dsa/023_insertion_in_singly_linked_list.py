"""
beginning - most efficient
create new node
point it to next node i.e. earlier first node
point head to new node

middle
traverse to the position sequentially
create new node
point previous node to it
point new node to next appropriate node

end - worst
traverse to last node
create new node
point last node to new node
point tail to new node

time = O(n) for traversal
space = O(1) for creating newnode and tempnode
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insert(self, value, location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
            elif location == -1:
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
                if tempnode == self.tail:
                    self.tail = newnode

singlylinkedlist = SLinkedList()
singlylinkedlist.insert(1, -1)  # start and end
singlylinkedlist.insert(2, -1)  # end
singlylinkedlist.insert(3, -1)  # end
singlylinkedlist.insert(4, -1)  # end
singlylinkedlist.insert(0, 0)  # start
singlylinkedlist.insert(0, 4)  # middle
print([node.value for node in singlylinkedlist])
