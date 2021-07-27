"""
operations:
create
enqueue
dequeue
peek
delete
ismepty
isfull

description:
FIFO
eg: queue at store
eg: token for restaurant order
eg: printer queue
eg: call center queue

creation:
list with no capacity - preferrable for smaller lists as enqueue may need moving and dequeue needs shifting
list with capacity - preferrable when we have enough space as list of fixed space is created with Nones
linkedlist - difficult implementation

creation(advanced):
- collections.deque - uses double linked lists - i.e. enqueues and dequeues in O(1)
deque()  # with or without capacity
append()  # when capacity is full, deletes first element to make space for new one
popleft()
clear()
- queue
- multiprocessing.Queue
"""
