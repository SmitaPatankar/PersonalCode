# binary tree with each layer full and bottom layer filled from left to right and every node <= its parent
# if implemented using list starting from index 1: 
# - every node's children are at node*2 and (node*2) + 1
# - similarly, every node's parent is node/2

# external
# push - O(log n)
#   - first - as is
#   - others - at bottom and float up as per root
# peek - O(1)
#   - blank - None
#   - filled - top
# pop - O(log n)
#   - blank - None
#   - one - as is
#   - multiple - swap with last - delete last - float top one down as per both children

# internal
# swap
# float_down
# bubble_up

class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self._bubble_down(len(self.heap)-1)

    def push(self, data):
            self.heap.append(data)
            self._float_up(len(self.heap)-1)

    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self._swap(len(self.heap)-1, 1)
            max = self.heap.pop()
            self._bubble_down(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _float_up(self, i):
        parent = i//2
        if i <= 1:
            return
        if self.heap[i] > self.heap[parent]:
            self._swap(i, parent)
            self._float_up(parent)

    def _bubble_down(self, i):
        left = i * 2
        right = (i * 2) + 1
        largest = i
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != i:
            self._swap(largest, i)
            self._bubble_down(largest)

    def __str__(self):
        return str(self.heap[1:])

print("create")
m = MaxHeap([95,3,21])
print(m)

print("push")
m.push(10)
print(m)

print("pop")
print(m.pop())
print(m)
