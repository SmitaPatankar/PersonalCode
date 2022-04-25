class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, node_data):
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, node_next):
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)


class UnOrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        previous = None
        current = self.head
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
        if current is None:
            raise ValueError(f"{item} is not in the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next


if __name__ == "__main__":
    my_list = UnOrderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(100))
    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())
    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))
    try:
        my_list.remove(27)
    except ValueError as ve:
        print(ve)

# todo
"""
The remaining methods append, insert, index, and pop are left as exercises. 
Remember that each of these must take into account whether the change is taking place at the head 
of the list or someplace else. 
Also, insert, index, and pop require that we name the positions of the list. 
We will assume that position names are integers starting with 0.

Part I: Implement the append method for UnorderedList. What is the time complexity of the method you created?

Part II: In the previous problem, you most likely created an append method that was O(n) If you add an instance variable to the UnorderedList class you can create an append method that is O(1). Modify your append method to be O(1) Be Careful! To really do this correctly you will need to consider a couple of special cases that may require you to make a modification to the add method as well.
"""
