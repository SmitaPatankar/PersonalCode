"""
check if head exists
start from head
traverse and check if element is found
terminate when found

time = O(n)
space = O(1) for one temporary node
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

    def traverse(self):
        if self.head is None:
            print("single linked list does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def search(self, nodevalue):
        if self.head is None:
            return "single linked list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    return node.value
                    break
                node = node.next
            return"not found"

singlylinkedlist = SLinkedList()
singlylinkedlist.insert(1, -1)
singlylinkedlist.insert(2, -1)
singlylinkedlist.insert(3, -1)
singlylinkedlist.insert(4, -1)
print(singlylinkedlist.search(2))
print(singlylinkedlist.search(5))
