# https://github.com/joeyajames/Python

#########
#builtin#
#########

t1 = (1,)
t2 = (2,)
print(t1+t2)  # (1, 2)

l = [1, 2]
print(l*3)  # [1, 2, 1, 2, 1, 2]

s = "smita"
print(sorted(s))  # ['a', 'i', 'm', 's', 't']

s = ["smita", "neha", "pooja"]
print(sorted(s, key=lambda x: x[-2]))  # ['neha', 'pooja', 'smita']

x = ["a", "b", "c"]
s1, s2, s3 = x
print(s1, s2, s3)  # a b c

x = [1, 2, 3]
del(x[1])
print(x)  # [1, 3]

x = [1, 2, 3]
del(x)
# print(x)  # NameError: name 'x' is not defined

x = [0, 2]
x.insert(1, "smita")
print(x)  # [0, 'smita', 2]

x.pop()
print(x)  # [0, 'smita']

x = [1, 2, 3, 4, 1]
x.remove(1)
print(x)  # [2, 3, 4, 1]

x = [1, 2, 3, 4, 1]
x.sort(reverse=True)
print(x)  # [4, 3, 2, 1, 1]

x = [1, 2, 3, 4, 1]
print(sorted(x, reverse=True))  # [4, 3, 2, 1, 1]

# tuples are faster than lists for finding items
x = ()
x = (1,)
x = 1,
x = (1, 2, 3)
x = 1, 2, 3
x = tuple([1, 2, 3])

# members of tuples can be mutable

# sets have non duplicate items
# items can be found instantly using hash no need to be sequential like list
# has faster access to items than list
# can do math set operations
# are unordered
x = {3, 4, 5, 3}
print(x)  # {3, 4, 5}
print(set([1, 2, 3]))  # {1,2,3}
x.add(6)
print(x)  # {3, 4, 5, 6}
x.remove(3)
print(x)  # {4, 5, 6}
x.pop() # random
print(x)  # {5, 6}
x.clear()
print(x)  # set()
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)  # {2, 3}
print(s1 | s2)  # {1, 2, 3, 4}
print(s1 ^ s2)  # {1, 4}
print(s1-s2)  # {1}
print(s1 <= s2)  # False
print(s1 >= s2)  # False

x = dict([(1, 2), (3, 4)])
print(x)  # {1: 2, 3: 4}

x = dict(s=2, d=4)
print(x)  # {'s': 2, 'd': 4}

x["smita"] = 5  # add or update
print(x)  # {'s': 2, 'd': 4, 'smita': 5}

del(x["smita"])
print(x)  # {'s': 2, 'd': 4}

print(len(x))  # 2

x.clear()
print(x)  # {}

del(x)
# print(x)  # NameError: name 'x' is not defined

x = {1: 2, 3: 4}
print(x.keys())  # dict_keys([1, 3])
print(x.values())  # dict_values([2, 4])
print(x.items())  # dict_items([(1, 2), (3, 4)])
print(1 in x)  # True
print(4 in x.values())  # True

for key in x:
    print(key, x[key])  # 1 2  # 3 4
for key, value in x.items():
    print(key, value)  # 1 2  # 3 4

s = "5m1t@"
print("".join([x for x in s if x.isnumeric()]))  # 51

import random
l = [1, 2, 3, 4, 5]
random.shuffle(l)
print(l)  # [3, 2, 1, 4, 5]

#######
#stack#
#######

"""
LIFO data structure
push, pop, peek and clear operations
eg: for undoing last command
"""

l = list()
l.append(0)
l.append(1)
l.append(2)
print(l)  # [0, 1, 2]
print(l.pop())  # 2
print(l.pop())  # 1

# can make wrapper class over it for Stack


class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)


s = Stack()
s.push(1)
s.push(2)
print(s)  # [1, 2]
print(s.pop())  # 2
print(s.peek())  # 1
print(s.pop())  # 1
print(s.pop())  # None

#######
#Queue#
#######

"""
FIFO data structure
enqueue, dequeue functions
eg: placing orders
"""

from collections import deque  # double ended queue  # can add and remove from both ends but we dont need that
q = deque()
q.append(1)
q.append(2)
print(q)  # deque([1, 2])
print(q.popleft())  # 1
print(q.popleft())  # 2

#########
#MaxHeap#
#########

"""
refer diagram
every node <= parent
so that highest number will always be on top and can be easily removed
they are fast for adding and removing items - O(log n) and for getting max - O(1)
every node's parent is at its index/2
every node's left child is at index*2
every node's right child is at (index*2)+1
push, pop and peek operation
push - add to end of array and float/bubble to proper position i.e. if it's greater than parent, swap and so on
peek - topmost element
pop - topmost element - swap first and last element - delete last element - bubble first element down to its correct position by comparing to its left child and swapping and so on
"""

# wrapper class with list
# public functions - push, peek and pop
# private functions - __swap, __floatUp, __bubbleDown, __str__
# starts at index 1


class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)


m = MaxHeap([95, 3, 21])
m.push(10)
print(m)  # [0, 95, 10, 21, 3]
print(m.pop())  # 95
print(m.peek())  # 21

#########
#minHeap#
#########

"""
similar to maxHeap with some modifications
"""


class MinHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            self.__swap(index, smallest)
            self.__bubbleDown(smallest)

    def __str__(self):
        return str(self.heap)


m = MinHeap([3, 21, 95])
m.push(10)
print(m)  # [0, 3, 10, 95, 21]
print(m.pop())  # 3
print(m.peek())  # 10

############
#linkedlist#
############

"""
fast operations
singly, doubly and circular
size is also an attribute of linkedlist
operations - find(data), add(data), remove(data), print_list()
singly:
    node has data and pointer to next node
    last node has no pointer(None)
    root pointer points to first node i.e. root node
    add:
        create node without pointer, make pointer as where root is pointing, change root to point to the new node
    remove:
        find the data from root, change previous node's pointer to point to found element's pointer
circular linked list:
    has pointer back to the root
    eg: for race track etc
    add:
        at second position
doubly:
    data, pointer to next node, pointer to previous node
    can iterate in either direction to save time when we know element is towards's end
    if we know pointer to an element, we can directly delete it
    has a last attribute also
"""


class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.previous_node = p

    def __str__(self):
        return str(f"({self.data})")


class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 1 if self.root else 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end="->")
            this_node = this_node.next_node
        print("None")


l = LinkedList()
l.add(5)
l.add(8)
l.add(12)
l.print_list()  # (12)->(8)->(5)->None
print(l.size)  # 3
l.remove(8)
print(l.size)  # 2
print(l.find(5))  # 5
print(l.root)  # (12)


class CircularLinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 1 if self.root else 0

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while True:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True
            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="->")
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end="->")
        print()


l = CircularLinkedList()
l.add(5)
l.add(7)
l.add(3)
l.add(8)
l.add(9)
print(l.size)  # 5
print(l.find(8))  # 8
print(l.find(12))  # False
l.print_list()  # (5)->(9)->(8)->(3)->(7)->
my_node = l.root
print(my_node, end="->")  # (5)->
for i in range(8):
    my_node = my_node.next_node
    print(my_node, end="->")  # (9)->(8)->(3)->(7)->(5)->(9)->(8)->(3)->
print()


class DoublyLinkedList:
    def __init__(self, r=None):
        self.root = r
        self.last = r
        self.size = 1 if self.root else 0

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.previous_node = new_node
            self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.previous_node is not None:
                    if this_node.next_node is not None:
                        this_node.previous_node.next_node = this_node.next_node
                        this_node.next_node.previous_node = this_node.previous_node
                    else:
                        this_node.previous_node.next_node = None
                        self.last = this_node.previous_node
                else:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True
            else:
                this_node = this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="->")
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print(this_node, end="->")
        print()


l = DoublyLinkedList()
l.add(5)
l.add(9)
l.add(3)
l.add(8)
l.add(9)
print(l.size)  # 5
l.print_list()  # (9)->(8)->(3)->(9)->(5)->
l.remove(8)
print(l.size)  # 4
l.remove(88)
print(l.find(88))  # None
l.add(21)
l.add(22)
l.remove(5)
l.print_list()  # (22)->(21)->(9)->(3)->(9)->
print(l.last.previous_node)  # (3)

##############
# Binary Tree#
##############

"""
see diagram

fast
eg: get person's number between 1 and 8 million
guess - 4 million - lower!
guess - 2 million  - higher!
guess - 3 million - lower!
3 guesses - reduced 7 millions - 1 million left
30 guesses - any data in 10million nodes tree

has nodes and edges
first node is root
parent and child nodes
sibling nodes
leaf nodes - no children
each node can have upto two children
subtree - part of tree that is a tree - bottom tree is sub tree of its parent
node's above a node are its ancestors and below ones are descendants
each node is greater than every node in its left subtree
each node is less than every node in its right subtree

operations - insert, find, delete, get_size, traversals
insert as a leaf at the correct position from root, insert below it's less than the element being compared, traverse to left sub tree, left subtree, right subtree
find from root if less than root, no, go to right subtree, less than yes, left subtree
delete - leaf node / node with 1 child, node with two children
    leaf - simply delete
    with one child - promote rest of the tree upwards
    with 2 children - take right subtree and left most node in the right subtree - swap main and last element and then delete last element
get_size - recursively - 1 + left subtree size + right subtree size
traversal:
    preorder - root - subtree - left subtree
    inorder - sorted - bottom left most to top and right

recursion - easy to implement
speed
find,delete, insert in O(heightoftree) or O(log n)
number of operations

Construction, Insert, Find, Get_size, Preorder, Inorder
"""


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True
    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1

    def preorder(self):
        if self is not None:
            print(self.data, end=" ")
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=" ")
            if self.right is not None:
                self.right.inorder()


t = Tree(7)
t.insert(9)
for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
    t.insert(i)
for i in range(16):
    print(t.find(i), end=" ")
    # False 1 2 3 4 False 6 7 False 9 10 11 12 13 14 15
print("\n", t.get_size())  # 13
t.preorder()
print()  # 7 2 1 3 6 4 9 15 10 12 11 13 14
t.inorder()
print()  # 1 2 3 4 6 7 9 10 11 12 13 14 15

#######
#graph#
#######

"""
vertices 
edges for relationships

undirected - by directional relationships - eg: people on social media, networking
directed - single directional relationships - eg: flights

ways of implementing graphs:
adjacency list - stores neighbors for each vertex in the vertex itself
adjacency matrix - 2d array of connections between vertices

dense graph - e = v square - adjacency list slower - matrix faster - lot of space - better for weighted edges
sparse graph - e = v - adjacency list is fast and takes less space
"""

# adjacency list

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, v, weight):
        if v not in self.neighbors:
            self.neighbors.append((v, weight))
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v, weight=0):
        if u in self.vertices and v in self.vertices:
            # my YouTube video shows a silly for loop here, but this is a much faster way to do it
            self.vertices[u].add_neighbor(v, weight)
            self.vertices[v].add_neighbor(u, weight)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ',
         'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()
# A[('B', 0), ('E', 0)]
# B[('A', 0), ('F', 0)]
# C[('G', 0)]
# D[('E', 0), ('H', 0)]
# E[('A', 0), ('D', 0), ('H', 0)]
# F[('B', 0), ('G', 0), ('I', 0), ('J', 0)]
# G[('C', 0), ('F', 0), ('J', 0)]
# H[('D', 0), ('E', 0), ('I', 0)]
# I[('F', 0), ('H', 0)]
# J[('F', 0), ('G', 0)]


# adjacency matrix

class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')


g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ',
         'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()
# A 0100100000
# B 1000010000
# C 0000001000
# D 0000100100
# E 1001000100
# F 0100001011
# G 0010010001
# H 0001100010
# I 0000010100
# J 0000011000
