# todo: improve programs
# todo: python: check: node with no reference will ideally go out of scope but still if needed delete it by making its next=None
# linked list
"""
linear data structure
collection of nodes

node has data and address of next node
last node points to null

for expanding array, new array gets created with more blocks and data gets copied over
not optimal
hence linked list

linked list is dynamic data structure
grow/shrink on runtime without wasting memory

no shifting needed for insertion and deletion in linked lists unlike arrays

in array elements had to be in continuous memory blocks as array points to address of first memory block
in linked lists, each node has address of next so continuous memory blocks are not needed - memory blocks anywhere in heap memory
head pointer points to first location
"""

# types of linked lists
"""
singly ll - node has data and next pointer
doubly ll - node has data and next pointer and previous pointer
circular ll - last node points to first node
circular doubly ll - last node points to first node, first node points to last
"""

# hw: handle tail for deleting last node
# hw: function to delete value
# singly linked list program
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class SinglyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def insert_at_head(self, data):
        print(f"inserting {data} at head")
        temp = Node(data)
        if not self.head:
            self.head = temp
            self.tail = temp
            return
        temp.next = self.head
        self.head = temp
    def insert_at_tail(self, data):
        print(f"inserting {data} at tail")
        temp = Node(data)
        if not self.tail:
            self.head = temp
            self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp
    def print(self):
        if not self.head:
            print("null")
            return
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("null")
    def insert_at_position(self, position, data):
            print(f"inserting {data} at {position}")
            if position == 0:
                self.insert_at_head(data)
                return
            if not self.head:
                print("invalid position")
                return
            count = 0
            temp = self.head
            while count < position-1:
                temp = temp.next
                if temp is None:
                    print("invalid position")
                    return
                count += 1
            if temp.next is None:
                self.insert_at_tail(data)
                return
            node_to_insert = Node(data)
            node_to_insert.next = temp.next
            temp.next = node_to_insert
    def delete_node(self, position):
        print(f"deleting at {position}")
        if not self.head:
            print("invalid position")
            return
        if position == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            if self.head is None:
                self.tail = None
            return
        count = 0
        prev_node = None
        current_node = self.head
        while count < position:
            prev_node = current_node
            current_node = current_node.next
            if current_node is None:
                print("invalid position")
                return
            count += 1
        prev_node.next = current_node.next
        current_node.next = None
        del current_node
        if prev_node.next is None:
            self.tail = prev_node
    def delete(self, data):
        print(f"deleting {data}")
        if not self.head:
            print("invalid data")
            return
        if data == self.head.data:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            if self.head is None:
                self.tail = None
            return
        prev_node = None
        current_node = self.head
        while current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
            if current_node is None:
                print("invalid value")
                return
        prev_node.next = current_node.next
        current_node.next = None
        del current_node
        if prev_node.next is None:
            self.tail = prev_node
try:
    s = SinglyLinkedList()
    s.insert_at_position(1, 3)
    s.print()
    s.insert_at_position(0, 3)
    s.print()
    s.insert_at_head(2)
    s.print()
    s.insert_at_head(1)
    s.print()
    s.insert_at_head(0)
    s.print()
    s.insert_at_tail(4)
    s.print()
    s.insert_at_tail(5)
    s.print()
    s.insert_at_position(3,2.5)
    s.print()
    s.insert_at_position(8,6)
    s.print()
    s.insert_at_position(0,-1)
    s.print()
    s.delete_node(0)
    s.print()
    s.delete_node(5)
    s.print()
    s.delete_node(6)
    s.print()
    s.delete_node(2)
    s.print()
    s.delete(0)
    s.print()
    s.delete(5)
    s.print()
    s.delete(2.5)
    s.print()
except Exception as e:
    print(f"--------------------------------------------->{e}")
"""

# hw: handle tail for deleting last node
# hw: function to delete value
# doubly linked list program
"""
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def print(self):
        if not self.head:
            print("null")
            return
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("null")
    def get_length(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length
    def insert_at_head(self, data):
        print(f"inserting {data} at head")
        temp = Node(data)
        if not self.head:
            self.head = temp
            self.tail = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
    def insert_at_tail(self, data):
        print(f"inserting {data} at tail")
        temp = Node(data)
        if not self.tail:
            self.head = temp
            self.tail = temp
            return
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
    def insert_at_position(self, position, data):
        print(f"inserting {data} at {position}")
        if position == 0:
            self.insert_at_head(data)
            return
        if not self.head:
            print("invalid position")
            return
        count = 0
        temp = self.head
        while count < position-1:
            temp = temp.next
            if temp is None:
                print("invalid position")
                return
            count += 1
        if temp.next is None:
            self.insert_at_tail(data)
            return
        node_to_insert = Node(data)
        node_to_insert.next = temp.next
        temp.next.prev = node_to_insert
        temp.next = node_to_insert
        node_to_insert.prev = temp
    def delete_node(self, position):
        print(f"deleting at {position}")
        if not self.head:
            print("invalid position")
            return
        if position == 0:
            temp = self.head
            if temp.next:
                temp.next.prev = None
            self.head = self.head.next
            temp.next = None
            del temp
            if self.head is None:
                self.tail = None
            return
        count = 0
        prev_node = None
        current_node = self.head
        while count < position:
            prev_node = current_node
            current_node = current_node.next
            if current_node is None:
                print("invalid position")
                return
            count += 1
        current_node.prev = None
        prev_node.next = current_node.next
        current_node.next = None
        if prev_node.next:
            prev_node.next.prev = None
        del current_node
        if prev_node.next is None:
            self.tail = prev_node
    def delete(self, data):
        print(f"deleting {data}")
        if not self.head:
            print("invalid data")
            return
        if data == self.head.data:
            temp = self.head
            if temp.next:
                temp.next.prev = None
            self.head = self.head.next
            temp.next = None
            del temp
            if self.head is None:
                self.tail = None
            return
        prev_node = None
        current_node = self.head
        while current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
            if current_node is None:
                print("invalid value")
                return
        prev_node.next = current_node.next
        current_node.next = None
        if prev_node.next:
            prev_node.next.prev = None
        del current_node
        if prev_node.next is None:
            self.tail = prev_node
try:
    d = DoublyLinkedList()
    d.insert_at_position(1, 3)
    d.print()
    d.insert_at_position(0, 3)
    d.print()
    d.insert_at_head(2)
    d.print()
    d.insert_at_head(1)
    d.print()
    d.insert_at_head(0)
    d.print()
    d.insert_at_tail(4)
    d.print()
    d.insert_at_tail(5)
    d.print()
    d.insert_at_position(3,2.5)
    d.print()
    d.insert_at_position(8,6)
    d.print()
    d.insert_at_position(0,-1)
    d.print()
    d.delete_node(0)
    d.print()
    d.delete_node(5)
    d.print()
    d.delete_node(6)
    d.print()
    d.delete_node(2)
    d.print()
    d.delete(0)
    d.print()
    d.delete(5)
    d.print()
    d.delete(2.5)
    d.print()
except Exception as e:
    print(f"--------------------------------------------->{e}")
"""

# circular ll program - mine
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class SinglyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def insert_at_head(self, data):
        print(f"inserting {data} at head")
        temp = Node(data)
        if not self.head:
            # circular
            temp.next = temp
            self.head = temp
            self.tail = temp
            return
        temp.next = self.head
        self.head = temp
        # circular
        self.tail.next = self.head
    def insert_at_tail(self, data):
        print(f"inserting {data} at tail")
        temp = Node(data)
        if not self.tail:
            # circular
            temp.next = temp
            self.head = temp
            self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp
        # circular
        self.tail.next = self.head
    def print(self):
        if not self.head:
            print("null")
            return
        print(f"{self.head.data if self.head else None}", end='     ')
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
            # circular
            if temp == self.head:
                break
        print("repeat", end="     ")
        print(f"{self.tail.data if self.tail else None}")
    def insert_at_position(self, position, data):
            print(f"inserting {data} at {position}")
            if position == 0:
                self.insert_at_head(data)
                return
            if not self.head:
                print("invalid position")
                return
            count = 0
            temp = self.head
            while count < position-1:
                temp = temp.next
                # circular
                if temp == self.head:
                    print("invalid position")
                    return
                count += 1
            # circular
            if temp.next == self.head:
                self.insert_at_tail(data)
                return
            node_to_insert = Node(data)
            node_to_insert.next = temp.next
            temp.next = node_to_insert
    def delete_node(self, position):
        print(f"deleting at {position}")
        if not self.head:
            print("invalid position")
            return
        if position == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            if self.head is None:
                self.tail = None
            else:
                self.tail.next = self.head
            return
        count = 0
        prev_node = None
        current_node = self.head
        while count < position:
            prev_node = current_node
            current_node = current_node.next
            # circular
            if current_node == self.head:
                print("invalid position")
                return
            count += 1
        prev_node.next = current_node.next
        current_node.next = None
        del current_node
        # circular
        if prev_node.next == self.head:
            self.tail = prev_node
    def delete(self, data):
        print(f"deleting {data}")
        if not self.head:
            print("invalid data")
            return
        if data == self.head.data:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            if self.head is None:
                self.tail = None
            else:
                self.tail.next = self.head
            return
        prev_node = None
        current_node = self.head
        while current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
            # circular
            if current_node == self.head:
                print("invalid value")
                return
        prev_node.next = current_node.next
        current_node.next = None
        del current_node
        # circular
        if prev_node.next == self.head:
            self.tail = prev_node
try:
    s = SinglyLinkedList()
    s.insert_at_position(1, 3)
    s.print()
    s.insert_at_position(0, 3)
    s.print()
    s.insert_at_head(2)
    s.print()
    s.insert_at_head(1)
    s.print()
    s.insert_at_head(0)
    s.print()
    s.insert_at_tail(4)
    s.print()
    s.insert_at_tail(5)
    s.print()
    s.insert_at_position(3,2.5)
    s.print()
    s.insert_at_position(8,6)
    s.print()
    s.insert_at_position(0,-1)
    s.print()
    s.delete_node(0)
    s.print()
    s.delete_node(5)
    s.print()
    s.delete_node(6)
    s.print()
    s.delete_node(2)
    s.print()
    s.delete(0)
    s.print()
    s.delete(5)
    s.print()
    s.delete(2.5)
    s.print()
except Exception as e:
    print(f"--------------------------------------------->{e}")
"""

# circular ll program
# using only tail
# inserting after a value
# not tracking start and end
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class CircularSinglyLinkedList:
    def __init__(self, tail=None):
        self.tail = tail
    def insert_node(self, element, data):
        print(f"inserting {data} after {element}")
        if not self.tail:
            if element is None:
                new_node = Node(data)
                self.tail = new_node
                new_node.next = new_node
            else:
                print("invalid element")
            return
        current_node = self.tail.next
        while current_node.data != element:
            current_node = current_node.next
            if current_node == self.tail.next:
                print("invalid element")
                return
        temp = Node(data)
        temp.next = current_node.next
        current_node.next = temp
        if current_node == self.tail:  # mine
            self.tail = temp
    def print(self):
        if not self.tail:
            print("null")
            return
        temp = self.tail.next
        print(temp.data, end="-->")
        temp = temp.next
        while temp != self.tail.next:
            print(temp.data, end="-->")
            temp = temp.next
        print("repeat", end="     ")
        print(f"{self.tail.data if self.tail else None}")
    def delete_node(self, data):
        print(f"deleting {data}")
        if not self.tail:
            print("invalid data")
            return
        prev_node = self.tail
        current_node = self.tail.next
        while current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
            if current_node == self.tail.next:
                print("invalid element")
                return
        if prev_node == current_node:
            self.tail = None
            return
        prev_node.next = current_node.next
        if current_node == self.tail:  # mine
            self.tail = prev_node
        current_node.next = None
        del current_node
try:
    cs = CircularSinglyLinkedList()
    cs.insert_node(5, 3)
    cs.print()
    cs.insert_node(None, 3)
    cs.print()
    cs.insert_node(3, 5)
    cs.print()
    cs.insert_node(5, 7)
    cs.print()
    cs.insert_node(5, 9)
    cs.print()
    cs.insert_node(10, 9)
    cs.print()
    cs.insert_node(5, 55)
    cs.print()
    cs.delete_node(9)
    cs.print()
    cs.delete_node(3)
    cs.print()
    cs.delete_node(7)
    cs.print()
    cs.delete_node(100)
    cs.print()
    cs.delete_node(5)
    cs.print()
    cs.delete_node(55)
    cs.print()
    cs.delete_node(7)
    cs.print()
except Exception as e:
    print(f"--------------------------------------------->{e}")
"""

# hw: doubly circular ll program
"""
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
class CircularDoublyLinkedList:
    def __init__(self, tail=None):
        self.tail = tail
    def insert_node(self, element, data):
        print(f"inserting {data} after {element}")
        if not self.tail:
            if element is None:
                new_node = Node(data)
                self.tail = new_node
                new_node.next = new_node
                new_node.previous = new_node
            else:
                print("invalid element")
            return
        current_node = self.tail.next
        while current_node.data != element:
            current_node = current_node.next
            if current_node == self.tail.next:
                print("invalid element")
                return
        temp = Node(data)
        temp.next = current_node.next
        current_node.next = temp
        temp.prev = current_node
        temp.next.prev = temp
        if current_node == self.tail:  # mine
            self.tail = temp
    def print(self):
        if not self.tail:
            print("null")
            return
        temp = self.tail.next
        print(temp.data, end="-->")
        temp = temp.next
        while temp != self.tail.next:
            print(temp.data, end="-->")
            temp = temp.next
        print("repeat", end="     ")
        print(f"{self.tail.data if self.tail else None}")
    def delete_node(self, data):
        print(f"deleting {data}")
        if not self.tail:
            print("invalid data")
            return
        prev_node = self.tail
        current_node = self.tail.next
        while current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
            if current_node == self.tail.next:
                print("invalid element")
                return
        if prev_node == current_node:
            self.tail = None
            return
        prev_node.next = current_node.next
        if current_node == self.tail:  # mine
            self.tail = prev_node
        prev_node.next.prev = prev_node
        current_node.next = None
        current_node.prev = None
        del current_node
try:
    cd = CircularDoublyLinkedList()
    cd.insert_node(5, 3)
    cd.print()
    cd.insert_node(None, 3)
    cd.print()
    cd.insert_node(3, 5)
    cd.print()
    cd.insert_node(5, 7)
    cd.print()
    cd.insert_node(5, 9)
    cd.print()
    cd.insert_node(10, 9)
    cd.print()
    cd.insert_node(5, 55)
    cd.print()
    cd.delete_node(9)
    cd.print()
    cd.delete_node(3)
    cd.print()
    cd.delete_node(7)
    cd.print()
    cd.delete_node(100)
    cd.print()
    cd.delete_node(5)
    cd.print()
    cd.delete_node(55)
    cd.print()
    cd.delete_node(7)
    cd.print()
except Exception as e:
    print(f"--------------------------------------------->{e}")
"""

# todo: hw: understand ll more https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms

# todo: tbd: practice linked list programs esp. below ones: https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms
# sort ll 0,1,2
# slow and fast pointer
# add one to linked list
# merge 2 sorted linked lists
# flatten multilevel linkedlist
# reverse linked list in k size groups ?
