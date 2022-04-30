# TODO: dsa: learn more about STL from here https://whimsical.com/c-stl-XVxuHHof5GTWA4NXZhXQhx (cpp)

# STL
"""
standard template library
library data structures, searching and sorting algorithms etc to not re-write everything again and again and also have it optimized
"""

# containers
"""
sequence containers
    array
    vector (cpp)
    deque
    list (cpp)
    forward_list (cpp)(rarely used)
container adaptors
    stack
    queue
    priority queue
associative containers
    set (cpp)
    map (cpp)
    multiset (cpp)(rarely used)
    multimap (cpp)(rarely used)
unordered associative containers
    set
    map
    multiset (cpp)(rarely used)
    multimap (cpp)(rarely used)
"""

# algorithms
"""
binary search
lower/upper bound
min/max
reverse/rotate
sort/swap
etc
"""

# array details
"""
static in cpp
data stored in contiguous memory locations
data is of similar type
complexity of specific element, is empty, front, back element is O(1) in cpp
"""

# TODO: python: program: array - size, loop,specific index, empty or not, first and last element - complexity of last element

# vector details (cpp)
"""
dynamic i.e. doubles size when full in cpp
creates new bigger vector, copies older elements and deletes older vector
shrink to fit to reduce it
"""

# TODO: python: program: list - fetching size and capacity of list as size increases, fetch specific element, fetch front and last element, pop, size and capacity after clear, get iterator of list, specify size already and initialize, copying lists

# deque details
"""
can insert and delete from front or back
not stored in contiguous memory locations - cpp
dynamic
random access is possible - cpp
"""

# TODO: python: program: check whether deque is stored in contiguous memory locations or not - check whether deque has random access - insert front back - pop front back - loop - print specific element - print front and back element - check if empty - get iterator - delete single or range of elements from start - check impact of erase on size and capacity

# list (doubly linked list) details (cpp)
"""
made using doubly linked list
front and back pointer
cant access elements directly using index - we'll have to travel
O(1) for empty, front fetch, back fetch etc
O(n) for erase as we have to go to each element - cpp
"""

# TODO: python: program : doubly linked list using self defined classes - make, add elements from back and front - print - iterator - empty - check complexity for erase - fetch from front back - loop - erase specific or range - size - copy - init with elements and size

# stack
"""
like stack of plates - LIFO - last in first out
"""

# TODO: python: program: stack: create, print top, pop, size,empty

# queue
"""
like line - FIFO - first in first out
front element fetch, pop, size, empty etc O(1)
"""

# TODO: python: program: queue using deque library - create, add, print front, pop, size, empty

# priority queue
"""
like max heap - default - can be made min
first element will always be greatest
when fetched, always max element will be fetched
"""

# TODO: python: program: priority queue: using library - make max/min, add elements one by one, loop and print and pop,size, empty

# set
"""
unique elements even if we add again and again
implement using binary search tree in cpp
can only add and delete but cannot modify in cpp
returned in sorted order in cpp
unordered set is faster in cpp
insert,find,erase,count is O(logn) in cpp for ordered set
size, begin, end, empty in cpp
"""

# TODO: python: program: unordered set: check how it's implemented in backend - create, insert, print in loop, add repeat, find, - check insert/find/erase/count/size/iterator/end/empty complexity, erase specific or range, iterator erase, count particular element, find iterator and print further

# map
"""
key value pair
unique keys
each key points to one value only
multiple keys can have same values
cpp has sorted and unsorted maps
insert, erase, find, count - O(logn) cpp ordered - implemented using red black tree or balanced tree
unordered one using hashtree there search is O(1) cpp
"""

# TODO: python: program: map type using dictionary - create, add,print in loop,insert value for key, insert kv pair, count of element, erase element - check insert erase find count complexity, iterator of find

# TODO: python: program: check how search is implemented: see if binary search is present for sorted array, take iterator for find using binary search, lower bound, upper bound using binary search using its iterator

# sort
"""
in cpp it uses quick sort, merge sort, insertion sort i.e. intro sort
"""

# TODO: python: program: max, min, swap, reverse string using its iterator, rotate vector using iterator put first to last, sort using iterator, check sort backend in python

# TODO: dsa: learn binary search tree, max heap, min heap, hashmap, red black tree, balanced tree, doubly linked list, merge sort, quick sort, stack, queue, priority queue etc and its complexities
