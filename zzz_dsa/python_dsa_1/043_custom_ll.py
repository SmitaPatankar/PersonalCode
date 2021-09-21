from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    # called on using str and print function
    def __str__(self):
        return str(self.value)


class CustomLL:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    # make iterable i.e. able to use for loop
    def __iter__(self):
        curnode = self.head
        while curnode:
            yield curnode
            curnode = curnode.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return "-> ".join(values)

    # called for len
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if not self.head:
            newnode = Node(value)
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min, max):
        for _ in range(n):
            self.add(randint(min, max))
        return self

customll = CustomLL()
customll.generate(10, 0, 99)
print(customll)
print(len(customll))
