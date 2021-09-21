"""
check if head exists
beginning
    create node with value and reference to null
    point node to head
    point head to node
    point tail to node
nth position
    create node with value and reference to null
    point node to next element
    point previous element to node
end
    create node with value and reference to null
    point node to first node
    point last node to node
    point tail to node

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

csll = CSLL()
print(csll.create(0))
print([i for i in csll])
csll.insert(1, -1)  # end
print([i for i in csll])
csll.insert(2, 0)  # start
print([i for i in csll])
csll.insert(3,1)  # middle
print([i for i in csll])
