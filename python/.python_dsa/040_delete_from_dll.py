"""
time = O(n)
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

    def insert(self, nodevalue, location):
        if not self.head:
            return "does not exist"
        newnode = Node(nodevalue)
        if location == 0:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        elif location == -1:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        else:
            tempnode = self.head
            index = 0
            while index < location - 1:
                tempnode = tempnode.next
                index += 1
            newnode.next = tempnode.next
            newnode.prev = tempnode
            newnode.next.prev = newnode
            tempnode.next = newnode

    def traverse(self):
        if not self.head:
            print("does not exist")
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next

    def reverse_traverse(self):
        if not self.head:
            print("does not exist")
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.prev

    def search(self, nodevalue):
        if not self.head:
            print("dll does not exist")
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodevalue:
                    return tempnode.value
                tempnode = tempnode.next
            return "not found"

    def delete(self, location):
        if not self.head:
            return "does not exist"
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            tempnode = self.head
            index = 0
            while index < location - 1:
                tempnode = tempnode.next
                index += 1
            tempnode.next = tempnode.next.next
            tempnode.next.prev = tempnode

dll = DLL()
print(dll.create(1))
print([i for i in dll])
dll.insert(0,0)
print([i for i in dll])
dll.insert(3, -1)
print([i for i in dll])
dll.insert(2,2)
print([i for i in dll])
dll.insert(4,-1)
print([i for i in dll])
dll.delete(0)
print([i for i in dll])
dll.delete(-1)
print([i for i in dll])
dll.delete(1)
print([i for i in dll])
