"""
self balancing binary search tree
difference between heights of left and right subtress cannot be more than one for all nodes

rotation - for balancing

need:
eg: 10 20 30 40 50 60 - very big one sided binary tree - O(N)
hence balance it to get O(logN)

create - same as binary search tree - O(1),O(1)
search - same as binary search tree - O(logn), O(logn)
traverse(4 ways) - same as binary search tree - O(n), O(n)
insert
    rotation reqd - if insertion is causing imbalance
        find node causing imbalance from below and also its grand child where height is more
        LL - rotate them right - O(1), O(1)
        LR - left rotation on left child and then right rotation like above - O(1), O(1)
        RR - left rotation - O(1), O(1)
        RL - right rotation on right child and then left rotation like above - O(1), O(1)
    rotation not reqd - if insertion is not causing imbalance
delete
    rotation not reqd
        leaf
        one child - move up
        two child - swap with successor
    rotation reqd
        LL
        LR
        RR
        RL
delete entire
"""

queue = __import__("052_queue_from_linkedlist_create_del_peek_enq_deq_isempty_isfull")

class Node:
    # O(1), O(1)
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1

# O(n), O(n)
def preordertraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preordertraversal(rootnode.leftchild)
    preordertraversal(rootnode.rightchild)

# O(n), O(n)
def inordertraversal(rootnode):
    if not rootnode:
        return
    inordertraversal(rootnode.leftchild)
    print(rootnode.data)
    inordertraversal(rootnode.rightchild)

# O(n), O(n)
def postordertraversal(rootnode):
    if not rootnode:
        return
    postordertraversal(rootnode.leftchild)
    postordertraversal(rootnode.rightchild)
    print(rootnode.data)

# O(n), O(n)
def levelordertraversal(rootnode):
    if not rootnode:
        return
    q = queue.Queue()
    q.enqueue(rootnode)
    while not q.isempty():
        qnode = q.dequeue()
        print(qnode.value.data)
        if qnode.value.leftchild:
            q.enqueue(qnode.value.leftchild)
        if qnode.value.rightchild:
            q.enqueue(qnode.value.rightchild)

# O(logn), O(logn)
def search(rootnode, nodevalue):
    if rootnode.data == nodevalue:
        print("found")
    elif nodevalue < rootnode.data:
        if rootnode.leftchild:
            if rootnode.leftchild.data == nodevalue:
                print("found")
            else:
                search(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        if rootnode.rightchild:
            if rootnode.rightchild.data == nodevalue:
                print("found")
            else:
                search(rootnode.rightchild, nodevalue)

def getheight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height

def rightrotation(disbnode):
    newroot = disbnode.leftchild
    disbnode.leftchild = disbnode.leftchild.rightchild
    newroot.rightchild = disbnode
    disbnode.height = 1 + max(getheight(disbnode.leftchild), getheight(disbnode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot

def leftrotation(disbnode):
    newroot = disbnode.rightchild
    disbnode.rightchild = disbnode.rightchild.leftchild
    newroot.leftchild = disbnode
    disbnode.height = 1 + max(getheight(disbnode.leftchild), getheight(disbnode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot

# O(1), O(1)
def getbalance(rootnode):
    if not rootnode:
        return 0
    return getheight(rootnode.leftchild) - getheight(rootnode.rightchild)

# O(logn), O(logn)
# learn more - write on own
def insert(rootnode, nodevalue):
    if not rootnode:
        rootnode = Node(nodevalue)
    elif nodevalue < rootnode.data:
        rootnode.leftchild = insert(rootnode.leftchild, nodevalue)
    else:
        rootnode.rightchild = insert(rootnode.rightchild, nodevalue)
    rootnode.height = 1 + max(getheight(rootnode.leftchild), getheight(rootnode.rightchild))
    balance = getbalance(rootnode)
    # left left
    if balance > 1 and nodevalue < rootnode.leftchild.data:
        return rightrotation(rootnode)
    # left right
    if balance > 1 and nodevalue > rootnode.rightchild.data:
        rootnode.leftchild = leftrotation(rootnode.leftchild)
        return rightrotation(rootnode)
    # right right
    if balance < -1 and nodevalue > rootnode.rightchild.data:
        return leftrotation(rootnode)
    # right left
    if balance < -1 and nodevalue < rootnode.rightchild.data:
        rootnode.rightchild = rightrotation(rootnode.rightchild)
        return leftrotation(rootnode)
    return rootnode

def getminnode(rootnode):
    if rootnode is None or rootnode.leftchild is None:
        return rootnode
    getminnode(rootnode.leftchild)

# learn more - write on own
# O(logn), O(logn)
def delete(rootnode, nodevalue):
    if not rootnode:
        return "empty"
    elif nodevalue < rootnode.data:
        rootnode.leftchild = delete(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        rootnode.rightchild = delete(rootnode.rightchild, nodevalue)
    else:
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        if rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        temp = getminnode(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = delete(rootnode.rightchild, temp.data)
    balance = getbalance(rootnode)
    if balance > 1 and balance(rootnode.leftchild) >= 0:
        return rightrotation(rootnode)
    if balance < -1 and balance(rootnode.rightchild) <= 0:
        return leftrotation(rootnode)
    if balance > 1 and balance(rootnode.leftchild) < 0:
        rootnode.leftchild = leftrotation(rootnode.leftchild)
        return rightrotation(rootnode)
    if balance < -1 and balance(rootnode.rightchild) > 0:
        rootnode.rightchild = rightrotation(rootnode.rightchild)
        return leftrotation(rootnode)
    return rootnode

# O(1), O(1)
def delete_entire(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return "deleted"

tree = Node(5)
search(tree, 5)
print("-----------------------------------------------------")
tree = insert(tree, 10)
tree = insert(tree, 15)
tree = insert(tree, 20)
levelordertraversal(tree)
print("-----------------------------------------------------")
tree = delete(tree, 15)
levelordertraversal(tree)
print("-----------------------------------------------------")
print(delete_entire(tree))
levelordertraversal(tree)
