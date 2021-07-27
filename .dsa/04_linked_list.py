# data and pointer to next node
# last node has next node as None
# root is pointer for first node

# get_size()
# find(data) - traverse
# add(data) - point new node to root node - point root to new node - increase size
# remove(data) - decrease size
# - doesnt exist - nothing
# - first node - point head to next of this node
# - between node - point previous node to this node's next node

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        node = Node(data, self.root)
        self.root = node
        self.size += 1

    def remove(self, data):
        node = self.root
        prev_node = None
        while node:
            if node.data == data:
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.root = node.next
                self.size -= 1
                return True
            else:
                prev_node = node
                node = node.next
        return False

    def find(self, data):
        node = self.root
        while node:
            if node.data == data:
                return data
            node = node.next
        return False

    def print(self):
        node = self.root
        while node:
            print(node.data, end="-->")
            node = node.next
        print("")

print("create")
l = LinkedList()
l.print()

print("add")
l.add(0)
l.print()

print("add")
l.add(1)
l.print()

print("add")
l.add(2)
l.print()

print("get size")
print(l.get_size())

print("find")
print(l.find(2))

print("remove")
l.remove(1)
l.print()
