"""
list of size with none everywhere
start = -1
stop = -1
start and stop pointers prevent shifting of elements
"""

class Queue:
    # O(1), O(n) for space of maxsize for list
    def __init__(self, maxsize):
        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.stop = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    # O(1), O(1)
    def isfull(self):
        if self.start == 0 and self.stop + 1 == self.maxsize:
            return True
        elif self.stop + 1 == self.start:
            return True
        else:
            return False

    # O(1), O(1)
    def isempty(self):
        if self.stop == -1:
            return True
        else:
            return False

    # O(1), O(1)
    def enqueue(self, value):
        if self.isfull():
            return "no space"
        else: 
            if self.stop + 1 == self.maxsize:
                self.stop = 0
            else:
                self.stop = self.stop + 1
                if self.start == -1:
                    self.start = 0
            self.items[self.stop] = value
            return "inserted"

    # O(1), O(1)
    def dequeue(self):
        if self.isempty():
            return "nothing to dequeue"
        firstelement = self.items[self.start]
        start = self.start
        if self.start == self.stop:
            self.start == -1
            self.stop == -1
        elif self.start + 1 == self.maxsize:
            self.start = 0
        else:
            self.start = self.start + 1
        self.items[start] = None
        return firstelement

    # O(1), O(1)
    def peek(self):
        if self.isempty():
            return "nothing to peek"
        return self.items[0]

    # O(1), O(1)
    def delete(self):
        self.items = self.maxsize * [None]
        self.start = -1
        self.stop = -1

q = Queue(5)
print(q)
print(q.isfull())
print(q.isempty())
print(q.enqueue(0))
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(5))
print(q)
print(q.dequeue())
print(q)
print(q.dequeue())
print(q)
print(q.enqueue(6))
print(q)
print(q.peek())
q.delete()
