# use single python list to implement 3 stacks

class Multistack:
    def __init__(self, stacksize=5, noofstacks=3):
        self.stacksize = stacksize
        self.noofstacks = noofstacks
        self.list = [0] * self.noofstacks * stacksize
        self.sizes = [0] * self.noofstacks

    def isfull(self, stackno):
        return self.sizes[stackno] == self.stacksize

    def isempty(self, stackno):
        return self.sizes[stackno] == 0

    def indexofll(self, stackno):
        offset = stackno * self.stacksize
        return offset + self.sizes[stackno] - 1

    def push(self, item, stackno):
        if self.isfull(stackno):
            return "full"
        self.sizes[stackno] += 1
        self.list[self.indexofll(stackno)] = item

    def pop(self, stackno):
        if self.isempty(stackno):
            return "empty"
        value = self.list[self.indexofll(stackno)]
        self.list[self.indexofll(stackno)] = 0
        self.sizes[stackno] -= 1
        return value

    def peek(self, stackno):
        if self.isempty(stackno):
            return "empty"
        return self.list[self.indexofll(stackno)]

m = Multistack()
print(m.isfull(1))
print(m.isempty(1))
print(m.push(0.0, 0))
print(m.push(0.1, 0))
print(m.push(1.0, 1))
print(m.push(1.1, 1))
print(m.pop(0))
print(m.peek(1))

# stack which has push, pop and min function with O(1)

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return f"{self.value}, {self.next}"

class Stack:
    def __init__(self):
        self.top = None
        self.minimum = None

    def min(self):
        return self.minimum.value
    
    def push(self, item):
        print(f"pushing {item}")
        if self.minimum and self.minimum.value < item:
            self.minimum = Node(self.minimum.value, next=self.minimum)
        else:
            self.minimum = Node(item, self.minimum)
        self.top = Node(item, self.top)

    def pop(self):
        if not self.top:
            return "no top"
        self.minimum = self.minimum.next
        item = self.top.value
        self.top = self.top.next
        return f"popping {item}"

print("---------------------------")
s = Stack()
s.push(0)
print(f"----->min is {s.min()}")
s.push(5)
print(f"----->min is {s.min()}")
s.push(-1)
print(f"----->min is {s.min()}")
s.push(10)
print(f"----->min is {s.min()}")
s.push(-2)
print(f"----->min is {s.min()}")
print("############################")
print(s.pop())
print(f"----->min is {s.min()}")
print(s.pop())
print(f"----->min is {s.min()}")
print(s.pop())
print(f"----->min is {s.min()}")
print(s.pop())
print(f"----->min is {s.min()}")

# set of stacks as per capacity - push, pop, popat

class StackSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)

    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and not len(self.stacks[-1]):
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def popat(self, stackno):
        if len(self.stacks[stackno]) > 0:
            return self.stacks[stackno].pop()
        else:
            return None

p = StackSet(2)
print(p)
p.push(1)
print(p)
p.push(2)
print(p)
p.push(3)
print(p)
p.push(4)
print(p)
print(p.pop())
print(p)
print(p.pop())
print(p)
print(p.pop())
print(p)
print(p.popat(0))
print(p)

# queue using 2 stacks
# for every queue operation, reverse the elements from one stack to other by popping
# then again put them back

class Stack:
    def __init__(self):
        self.list = []
    
    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()

class Queue:
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def enqueue(self, item):
        self.instack.push(item)

    def dequeue(self):
        while len(self.instack):
            self.outstack.push(self.instack.pop())
        item = self.outstack.pop()
        while len(self.outstack):
            self.instack.push(self.outstack.pop())
        return item

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())

# FIFO queue with dogs and cats
# enqueue
# dequedog
# dequecat
# dequeany

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == "cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    
    def dequecat(self):
        if len(self.cats) == 0:
            return None
        else:
            return self.cats.pop(0)

    def dequedog(self):
        if len(self.dogs) == 0:
            return None
        else:
            return self.dogs.pop(0)

    def dequeany(self):
        if len(self.cats):
            return self.cats.pop(0)
        else:
            return self.dogs.pop(0)

q = AnimalShelter()
q.enqueue("cat1", "cat")
q.enqueue("cat2", "cat")
q.enqueue("dog1", "dog")
q.enqueue("cat3", "cat")
q.enqueue("dog2", "dog")
print(q.dequecat())
print(q.dequedog())
print(q.dequedog())
print(q.dequeany())
