"""
complete binary tree with some additional properties

complete binary tree:
0, 1 or 2 nodes
all levels full or except last one which is as last as possible

as it's complete, it is ideal for arrays and lists as there are no gaps

min heap - root is min among all values recursively
max heap - root is max among all values recursively

find min or max in logn time
insert in logn time

create - fixed size array, size of heap = 0
peek - first element
traverse - 4 types - level order
size - saved size
insert - size + 1 - bubble up if small
delete - size - 1  - only top - replace with bottom element and bubble down

data structure:
array (2x, 2x+1, x is node, root is 1)
reference pointer (possible)
"""

class Heap:
    # O(1), O(n)
    def __init__(self, size):
        self.maxsize = size + 1
        self.customlist = self.maxsize * [None]
        self.heapsize = 0

# O(1), O(1)
def peek(rootnode):
    if not rootnode:
        return
    return rootnode.customlist[-1]

# O(1), O(1)
def sizeofheap(rootnode):
    if not rootnode:
        return
    return rootnode.heapsize

# O(n), O(1)
def levelordertraversal(rootnode):
    if not rootnode:
        return
    for i in range(1, rootnode.heapsize+1):
        print(rootnode.customlist[i])

# O(logn), O(logn)
def heapifyinsert(rootnode, index, heaptype):
    parentindex = int(index/2)
    if index <= 1:
        return
    if heaptype == "min":
        if rootnode.customlist[index] < rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
            return heapifyinsert(rootnode, parentindex, heaptype)
    if heaptype == "max":
        if rootnode.customlist[index] > rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
            return heapifyinsert(rootnode, parentindex, heaptype)

def insert(rootnode, nodevalue, heaptype):
    if rootnode.heapsize + 1 == rootnode.maxsize:
        return "full"
    rootnode.customlist[rootnode.heapsize + 1] = nodevalue
    rootnode.heapsize += 1
    heapifyinsert(rootnode, rootnode.heapsize, heaptype)
    return "inserted"

# O(logn), O(logn)
def heapifydelete(rootnode, index, heaptype):
    leftchildindex = int(index*2)
    rightchildindex = int(index*2)+1
    swapchild = 0
    if rootnode.heapsize < leftchildindex:
        return
    elif rootnode.heapsize == leftchildindex:
        if heaptype == "min":
            if rootnode.customlist[index] > rootnode.customlist[leftchildindex]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftchildindex]
                rootnode.customlist[leftchildindex] = temp
            return
        else:
            if rootnode.customlist[index] < rootnode.customlist[leftchildindex]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftchildindex]
                rootnode.customlist[leftchildindex] = temp
            return       
    else:
        if heaptype == "min":
            if rootnode.customlist[leftchildindex] < rootnode.customlist[rightchildindex]:
                swapchild = leftchildindex
            else:
                swapchild = rightchildindex
            if rootnode.customlist[index] > rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp
            return
        else:
            if rootnode.customlist[leftchildindex] > rootnode.customlist[rightchildindex]:
                swapchild = leftchildindex
            else:
                swapchild = rightchildindex
            if rootnode.customlist[index] < rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp
        heapifydelete(rootnode, swapchild, heaptype)

# O(logn), O(logn)
def delete(rootnode, heaptype):
    if rootnode.heapsize == 0:
        return
    extracted_node = rootnode.customlist[1]
    rootnode.customlist[1] = rootnode.customlist[rootnode.heapsize]
    rootnode.customlist[rootnode.heapsize] = None
    rootnode.heapsize -= 1
    heapifydelete(rootnode, 1, heaptype)
    return extracted_node

# O(1), O(1)
def delete_entire(rootnode):
    rootnode.customlist = None

h = Heap(5)
insert(h, 4, "min")
insert(h, 5, "min")
insert(h, 2, "min")
insert(h, 1, "min")
print(peek(h))
print(sizeofheap(h))
print("-----------------------------------")
levelordertraversal(h)
delete(h, "min")
print("-----------------------------------")
levelordertraversal(h)
delete_entire(h)
