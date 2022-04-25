from p0024_unordered_linked_list import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next
        return False

    def add(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        while current is not None and current.data < item:
            previous = current
            current = current.next
        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    my_list = OrderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(100))

# todo
"""
We leave the remaining methods as exercises. 
You should carefully consider whether the unordered implementations will work given that the list is 
now ordered.

https://runestone.academy/runestone/books/published/pythonds3/BasicDS/DiscussionQuestions.html

https://runestone.academy/runestone/books/published/pythonds3/BasicDS/Exercises.html
"""
