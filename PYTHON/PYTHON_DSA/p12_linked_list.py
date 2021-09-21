class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LL:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, data):
        node = Node(data, self.root)
        self.root = node
        self.size += 1

    def remove(self, data):
        prev = None
        node = self.root
        while node:
            if node.data == data:
                if prev:
                    prev.next_node = node.next_node
                else:
                    self.root = node.next_node
                self.size -= 1
                return True
            prev = node
            node = node.next_node
        return False

    def find(self, data):
        node = self.root
        while node:
            if node.data == data:
                return data
            node = node.next_node
        return None

    def get_size(self):
        return self.size

    def print(self):
        pointer = self.root
        while pointer:
            print(pointer.data, end="-->")
            pointer = pointer.next_node
        print()


print("creating linked list i.e. with root node having data and next as None and size as 0")
ll = LL()
ll.print()

print("adding elements")
ll.add(0)
ll.print()
ll.add(1)
ll.print()
ll.add(2)
ll.print()

print("finding element")
print(ll.find(1))
print(ll.find(1000))

print("removing element")
ll.remove(1)
ll.print()
ll.remove(10000)

print("getting size")
print(ll.get_size())
