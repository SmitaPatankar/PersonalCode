class Queue:
    # O(1), O(1)
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    # O(1), O(1)
    def isempty(self):
        if self.items == []:
            return True
        else:
            return False

    # O(1)/O(n)/O(n^2) when array is moved on reaching capacity, O(1)
    def enqueue(self, value):
        self.items.append(value)

    # O(n) for shifting elements backwards, O(1)
    def dequeue(self):
        if self.isempty():
            return "nothing to dequeue"
        return self.items.pop(0)

    # O(1), O(1)
    def peek(self):
        if self.isempty():
            return "nothing to peek"
        return self.items[0]

    # O(1), O(1)
    def delete(self):
        self.items = None

q = Queue()
print(q)
print(q.isempty())
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
print(q.dequeue())
print(q)
print(q.peek())
q.delete()
