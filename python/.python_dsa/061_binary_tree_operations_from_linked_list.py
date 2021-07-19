"""
create tree - node with value only
traverse nodes
    DFS
        preorder - root, left subtree, right subtree
        inorder - left, root, right
        postorder - left, right, root
    BFS
        level order traversal - root, left, right, its left right, so on
search node - level order traversal
insert node - blank root : create, tree exists: add on first vacant place in level order
delete node - replace wanted node with deepest node then delete deepest
delete tree - with ll, set root to none and delete links between root and left and right child
"""


queue = __import__("052_queue_from_linkedlist_create_del_peek_enq_deq_isempty_isfull")

class Node:
    # O(1), O(1)
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

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

# level order traversal because others save recursion calls in stack memory
# O(n), O(n)
def search(rootnode, searchvalue):
    if not rootnode:
        return
    q = queue.Queue()
    q.enqueue(rootnode)
    while not q.isempty():
        root = q.dequeue()
        if root.value.data == searchvalue:
            return root.value.data
        if root.value.leftchild:
            q.enqueue(root.value.leftchild)
        if root.value.rightchild:
            q.enqueue(root.value.rightchild)
    return "not found"

# O(n), O(n)
def insert(rootnode, insertnode):
    if not rootnode:
        rootnode = insertnode
        return "inserted"
    q = queue.Queue()
    q.enqueue(rootnode)
    while not q.isempty():
        root = q.dequeue()
        if root.value.leftchild:
            q.enqueue(root.value.leftchild)
        else:
            root.value.leftchild = insertnode
            return "inserted"
        if root.value.rightchild:
            q.enqueue(root.value.rightchild)
        else:
            root.value.leftchild = insertnode
            return "inserted"

# O(n), O(n)
def getdeepestnode(rootnode):
    if not rootnode:
        return
    q = queue.Queue()
    q.enqueue(rootnode)
    while not q.isempty():
        root = q.dequeue()
        if root.value.leftchild:
            q.enqueue(root.value.leftchild)
        if root.value.rightchild:
            q.enqueue(root.value.rightchild)
    deepestnode = root.value
    return deepestnode

def deletedeepestnode(rootnode, deepestnode):
    if not rootnode:
        return
    q = queue.Queue()
    q.enqueue(rootnode)
    while not q.isempty():
        root = q.dequeue()
        if root.value is deepestnode:
            root.value = None
            return
        if root.value.rightchild:
            if root.value.rightchild is deepestnode:
                root.value.rightchild = None
                return
            else:
                q.enqueue(root.value.rightchild)
        if root.value.leftchild:
            if root.value.leftchild is deepestnode:
                root.value.leftchild = None
                return
            else:
                q.enqueue(root.value.leftchild)

# learn more about messed up order
# O(n), O(n)
def deletenode(rootnode, delnode):
    if not rootnode:
        return "no tree"
    deepestnode = getdeepestnode(rootnode)
    q = queue.Queue()
    q.enqueue(rootnode)
    while not q.isempty():
        root = q.dequeue()
        if root.value.data == delnode.data:
            root.value.data = delnode.data
            deletedeepestnode(rootnode, deepestnode)
            return "deleted"
        if root.value.rightchild:
            q.enqueue(root.value.rightchild)
        if root.value.leftchild:
            q.enqueue(root.value.leftchild)
    return "failed to delete"

# O(1), O(1)
def delete_entire(rootnode):
    if not rootnode:
        return "empty"
    rootnode.leftchild = None
    rootnode.rightchild = None
    rootnode.data = None
    return "deleted"

drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
drinks.leftchild = hot
drinks.rightchild = cold
preordertraversal(drinks)
print("#########")
inordertraversal(drinks)
print("#########")
postordertraversal(drinks)
print("#########")
levelordertraversal(drinks)
print("#########")
print(search(drinks, "cold"))
print(search(drinks, "blah"))
print("#########")
somedrink = Node("somedrink")
insert(drinks, somedrink)
levelordertraversal(drinks)
print("#########")
deepestnode = getdeepestnode(drinks)
deletedeepestnode(drinks, deepestnode)
levelordertraversal(drinks)
print("#########")
deletenode(drinks, hot)
levelordertraversal(drinks)
print("#########")
print(delete_entire(drinks))
levelordertraversal(drinks)
