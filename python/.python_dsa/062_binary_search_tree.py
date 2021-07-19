"""
description:
has additional properties than binary tree
left subtree values are less than or equal to parent
right subtree values are greater than or equal to parent

pros:
quick insertion and deletion
half - half - half

operations:
create - node with empty data, empty left child, empty right child
insert - find correct spot by traversing from root
traverse(4 ways) - same as binary tree
search - traverse left or right depending on small or big
delete node
    leaf - search and delete directly
    with one child - search and just delete and move the child upwards
    with two children - find second largest element to that i.e. smallest node in right subtree, swap and delete
delete tree - make root node data, leftchild and rightchild as none

data structure used:
linked list
list (possible)
"""

queue = __import__("052_queue_from_linkedlist_create_del_peek_enq_deq_isempty_isfull")

class Node:
    # O(1), O(1)
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

# O(logn), O(logn)
def insert(rootnode, value):
    if rootnode.data == None:
        rootnode.data = value
    elif value <= rootnode.data:
        if rootnode.leftchild == None:
            rootnode.leftchild = Node(value)
        else:
            insert(rootnode.leftchild, value)
    else:
        if rootnode.rightchild == None:
            rootnode.rightchild = Node(value)
        else:
            insert(rootnode.rightchild, value)
    return "inserted"

# O(n) - half trees traversed on both sides, O(n)
def preordertraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preordertraversal(rootnode.leftchild)
    preordertraversal(rootnode.rightchild)

# O(n) - half trees traversed on both sides, O(n)
def inordertraversal(rootnode):
    if not rootnode:
        return
    inordertraversal(rootnode.leftchild)
    print(rootnode.data)
    inordertraversal(rootnode.rightchild)

# O(n) - half trees traversed on both sides, O(n)
def postordertraversal(rootnode):
    if not rootnode:
        return
    postordertraversal(rootnode.leftchild)
    postordertraversal(rootnode.rightchild)
    print(rootnode.data)

# O(n) - half trees traversed on both sides, O(n)
def levelordertraversal(rootnode):
    if not rootnode:
        return
    q = queue.Queue()
    q.enqueue(rootnode)
    while not q.isempty():
        root = q.dequeue()
        print(root.value.data)
        if root.value.leftchild:
            q.enqueue(root.value.leftchild)
        if root.value.rightchild:
            q.enqueue(root.value.rightchild)

# O(logn), O(logn)
# learn more about elements equal to the one present in list
# write on own - learn more
def search(rootnode, value):
    if rootnode:
        if rootnode.data == value:
            print("found")
        elif value < rootnode.data:
            if rootnode.leftchild:
                if rootnode.leftchild.data == value:
                    print("found")
                else:
                    search(rootnode.leftchild, value)
        elif rootnode.rightchild:
            if rootnode.rightchild.data == value:
                print("found")
            else:
                search(rootnode.rightchild, value)

def minvaluenode(node):
    currentnode = node
    while currentnode.leftchild:
        currentnode = currentnode.leftchild
    return currentnode

# O(logn) , O(logn) - learn more
# write on own - learn more
def deletenode(rootnode, nodevalue):
    if not rootnode:
        return None
    if nodevalue < rootnode.data:
        rootnode.leftchild = deletenode(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        rootnode.rightchild = deletenode(rootnode.rightchild, nodevalue)
    else:
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        if rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        temp = minvaluenode(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = deletenode(rootnode.rightchild, temp.data)
    return rootnode

# O(1), O(1)
def delete(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return "deleted"

n = Node(None)
print(insert(n, 70))
print(insert(n, 50))
print(insert(n, 90))
print(insert(n, 30))
print(insert(n, 60))
print(insert(n, 80))
print(insert(n, 100))
print(insert(n, 20))
print(insert(n, 40))
print(insert(n, 95))
print(insert(n, 105))
print("####################")
preordertraversal(n)
print("####################")
inordertraversal(n)
print("####################")
postordertraversal(n)
print("####################")
levelordertraversal(n)
print("####################")
search(n, 0)
print("####################")
deletenode(n, 90)
levelordertraversal(n)
print("####################")
print(delete(n))
levelordertraversal(n)
