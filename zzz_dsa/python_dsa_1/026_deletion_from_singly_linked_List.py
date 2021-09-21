"""
check if head exists
first node
    only node
        point head to null
        point tail to null
    more nodes
        point head to 2nd node
given location node
    traverse till previous node
    point previous node to next node
last node
    one node
        point head to null
        point tail to null
    more nodes
        traverse till 2nd last node
        point second last node to null
        point tail to second last node

time = O(n)
space = O(1)
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

    def delete(self, location):
        if not self.head:
            return "singly linked list does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    print(f"head is {self.head.value}")
                    print(f"pointing head to {self.head.next.value}")
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                             break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = nextnode.next
                # mine
                # if tempnode.next == None:
                #     self.tail = tempnode

singlylinkedlist = SLinkedList()
singlylinkedlist.insert(0, -1)
singlylinkedlist.insert(1, -1)
singlylinkedlist.insert(2, -1)
singlylinkedlist.insert(3, -1)
singlylinkedlist.insert(4, -1)
singlylinkedlist.insert(5, -1)
print([node.value for node in singlylinkedlist])
singlylinkedlist.delete(0)
print([node.value for node in singlylinkedlist])
singlylinkedlist.delete(-1)
print([node.value for node in singlylinkedlist])
singlylinkedlist.delete(2)
print([node.value for node in singlylinkedlist])
