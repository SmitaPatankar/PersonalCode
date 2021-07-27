"""
time = O(n)
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
            node = node.next
            if node == self.tail.next:
                break
            
    def create(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return "created"

    def insert(self, value, location):
        if not self.head:
            return "does not exist"
        else:
            newnode = Node(value)
            if location == 0:
                newnode.next = self.head
                self.head = newnode
                self.tail.next = newnode
            elif location == -1:
                newnode.next = self.tail.next
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

    def traverse(self):
        if not self.head:
            print("does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break

    def search(self, nodevalue):
        if not self.head:
            print("does not exist")
        else:
            node = self.head
            while node:
                node = node.next
                if node.value == nodevalue:
                    return(node.value)
                node = node.next
                if node == self.tail.next:
                    return "not found"

    def delete(self, location):
        if not self.head:
            print("does not exist")
        elif location == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif location == -1:
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = self.head
                self.tail = node
        else:
            tempnode = self.head
            index = 0
            while index < location - 1:
                tempnode = tempnode.next
                index += 1
            nextnode = tempnode.next
            tempnode.next = nextnode.next                        

csll = CSLL()
print(csll.create(0))
print([i for i in csll])
csll.insert(1, -1)  # end
print([i for i in csll])
csll.insert(2, 0)
print([i for i in csll])
csll.insert(3,1)
print([i for i in csll])
csll.insert(4,1)
print([i for i in csll])
csll.insert(5,1)
print([i for i in csll])
csll.delete(0)
print([i for i in csll])
csll.delete(-1)
print([i for i in csll])
csll.delete(2)
print([i for i in csll])
