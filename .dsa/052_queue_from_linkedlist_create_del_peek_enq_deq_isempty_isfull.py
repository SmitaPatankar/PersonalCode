class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Queue:
    # O(1), O(1)
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.ll]
        return " ".join(values)

    # O(1), O(1)
    def enqueue(self, value):
        node = Node(value)
        if not self.ll.head:
            self.ll.head = node
            self.ll.tail = node
        else:
            self.ll.tail.next = node
            self.ll.tail = node

    # O(1), O(1)
    def isempty(self):
        return True if not self.ll.head else False

    # O(1), O(1)
    def dequeue(self):
        if self.isempty():
            return "nothing to dequeue"
        else:
            if self.ll.head == self.ll.tail:
                value = self.ll.head
                self.ll.head = None
                self.ll.tail = None
            else:
                value = self.ll.head
                self.ll.head = self.ll.head.next
            return value

    # O(1), O(1)
    def peek(self):
        if self.isempty():
            return "nothing to dequeue"
        return self.ll.head

if __name__ == "__main__":
    q = Queue()
    print(q)
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.peek())
