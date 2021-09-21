class MaxHeap:
    def __init__(self, items=None):
        self.lst = [None]
        if items:
            for item in items:
                self.push(item)

    def push(self, element):
        self.lst.append(element)
        self.float_up(len(self.lst) - 1)

    def peek(self):
        if len(self.lst) > 1:
            return self.lst[1]
        return None

    def pop(self):
        if len(self.lst) == 1:
            return False
        if len(self.lst) == 2:
            return self.lst.pop()
        self.swap(1, -1)
        max_element = self.lst.pop()
        self.bubble_down(1)
        return max_element

    def swap(self, i, j):
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]

    def float_up(self, index):
        if index <= 1:
            return
        parent = index // 2
        if self.lst[index] > self.lst[parent]:
            self.swap(index, parent)
            self.float_up(parent)

    def bubble_down(self, index):
        left = index * 2
        right = (index * 2) + 1
        largest = index
        if len(self.lst) > left and self.lst[left] > self.lst[largest]:
            largest = left
        if len(self.lst) > right and self.lst[right] > self.lst[largest]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.bubble_down(largest)


print("creating max heap")
h = MaxHeap([1, 2, 10, 20, 30, 0, 5])
print(h.lst)

print("pushing item")
h.push(50)
print(h.lst)

print("popping item")
h.pop()
print(h.lst)

print("peeking item")
print(h.peek())
