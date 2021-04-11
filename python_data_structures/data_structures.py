"""
https://github.com/codebasics/data-structures-algorithms-python - bigocheatsheet.com

data stored as binary in RAM
1 byte has one address location
int takes 4 bytes i.e. 32 bits

basic data type - list
    search by index - initial location + index * 4
    search by data - sequential
    insert - shifts locations of elements thereafter, initial capacity and copies and increases when needed bcoz space around current locations is taken up by some other program
    delete - shifts locations of elements thereafter

to solve the insert capacity problem in list - linked list
    search by index - not exactly supported
    search by value - sequential
    insert - sequential, no need to manage space
    delete - sequential

to solve the search by data problem in nested list - hashmap(like dictionary) - saves at hash location in capacity
hash function like mod of sum of ascii chars div by 100 assuming length is 100
__setitem__, __getitem__ and __delitem__ lets us use it like x["smita"] i.e. as index operators
    search by index - not supported
    search by data - direct
    insert - direct
    delete - direct
collisions can be handled by chaining linked lists so that multiple keys have same index, but that will increase time
collisions can be handled by linear probing i.e. save on next available location in capacity

for popping last element without overhead of list and linkedlist - stack
eg: browser back button, word undo button
can be implemented using list(not recommended due to capacity)
can be implemented using collections.deque(recommended as they use doubly linked list internally)
can be implemented using queue.LifoQueue
    push - direct
    pop - direct
    search - sequential

for loosely coupled architecture - queue
eg: for stock exchange to send information to various servers which the servers can pull
can be implemented using list(not recommended due to capacity)
can be implemented using collections.deque(recommended)
can be implemented using queue.LifoQueue
    search by value  - sequential
    enqueue - direct
    dequeue - direct

for hierarchical data - general tree
eg: online shopping categories, organization chart, folder structure
can be implemented as a class

for hierarchical data with upto 2 children for each node with some order for quicker search - binary tree
LHS of any node is lesser than itself and RHS
no duplicate elements
    search - each time search is reduced by half - search from root if less than that go to left else right so on
        breadth first search
        depth first search
            in order - left, root, right
            pre order - root, left, right
            post order - left, right, root
    insert - quick enough
    delete - quick enough (move min from right or max from left up)
    sort - quick enough
useful for implementing sets
can be implemented using class

for connected data - graph
eg: social networking for suggesting friends, flights for finding shortest route, maps, networking
can be implemented using class
"""