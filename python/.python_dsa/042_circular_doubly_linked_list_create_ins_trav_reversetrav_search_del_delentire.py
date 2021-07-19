"""
traverse backwards + go from last node to first node or vice versa

create
time = O(1)
space = O(1)

insert
time = O(n)
space = O(1)

traverse
time = O(n)
space = O(1)

search
time = O(n)
space = O(1)

delete
time = O(n)
space = O(1)

delete entire
time = O(n)
space = O(1)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            if node == self.tail.next:
                break
    
    def create(self, nodevalue):
        newnode = Node(nodevalue)
        self.head = newnode
        self.tail = newnode
        newnode.next = newnode
        newnode.prev = newnode

    def insert(self, value, location):
        if not self.head:
            print("cdll does not exist")
        else:
            newnode = Node(value)
            if location == 0:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.head = newnode
                self.tail.next = newnode
            elif location == -1:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
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
            print("cdll does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                if node == self.tail:
                    break
                node = node.next

    def reverse_traverse(self):
        if not self.head:
            print("cdll does not exist")
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev

    def search(self, nodevalue):
        if not self.head:
            print("cdll does not exist")
        else:
            node = self.head
            while node:
                if node.value == nodevalue:
                    return node.value
                if node == self.tail:
                    return "not found"
                node = node.next

    def delete(self, location):
        if not self.head:
            print("cdll does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None                
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None                
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                if not self.head:
                    return "cdll does not exist"
                else:
                    tempnode = self.head
                    index = 0
                    while index < location - 1:
                        tempnode = tempnode.next
                    tempnode.next = tempnode.next.next
                    tempnode.next.prev = tempnode

    def delete_entire(self):
        if not self.head:
            print("csll does not exist")            
        else:
            self.tail.next = None
            tempnode = self.head
            while tempnode:
                tempnode.prev = None
                tempnode = tempnode.next       
            self.head = None
            self.tail = None

cdll = CDLL()
cdll.create(4)
print([i for i in cdll])
cdll.insert(3, 0)
print([i for i in cdll])
cdll.insert(2, 0)
print([i for i in cdll])
cdll.insert(2.5,1)
print([i for i in cdll])
cdll.insert(5, -1)
print([i for i in cdll])
cdll.traverse()
cdll.reverse_traverse()
print(cdll.search(2))
print(cdll.search(100))
cdll.delete(0)
print([i for i in cdll])
cdll.delete(-1)
print([i for i in cdll])
cdll.delete(1)
print([i for i in cdll])
cdll.delete_entire()
print([i for i in cdll])
