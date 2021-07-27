# both tree and node helper
# insert - if smaller insert in left side else right
# find - if smaller search in left side else right
# preorder traversal - root left right
# inorder traversal - left root right
# postorder traversal - left right root
# remove - note parent, node, child
#  - tree is empty - do nothing
#  - value is not present - do nothing
#  - value is present at root and tree has only root - simply delete
#  - node has only one child - move up
#  - node has both children - note delnode(lowest value in node's right subtree), delparent -> swap, delete recursively

class Node:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None

    def insert(self, newvalue):
        if self.value == newvalue:
            return False
        elif newvalue < self.value:
            if self.leftchild:
                return self.leftchild.insert(newvalue)
            else:
                self.leftchild = Node(newvalue)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(newvalue)
            else:
                self.rightchild = Node(newvalue)
                return True  

    def find(self, findvalue):
        if findvalue == self.value:
            return findvalue
        elif findvalue < self.value:
            if self.leftchild:
                self.leftchild.find(findvalue)
            else:
                return False
        else:
            if self.rightchild:
                self.rightchild.find(findvalue)
            else:
                return False

    def preorder(self):
        print(self.value)
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        print(self.value)
        if self.rightchild:
            self.rightchild.inorder()

    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        print(self.value)

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, insertvalue):
        if self.root:
            return self.root.insert(insertvalue)
        else:
            self.root = Node(insertvalue)
            return True

    def find(self, findvalue):
        if self.root:
            return self.root.find(findvalue)
        else:
            return False

    def preorder(self):
        if self.root:
            self.root.preorder()
        else:
            return False

    def inorder(self):
        if self.root:
            self.root.inorder()
        else:
            return False

    def postorder(self):
        if self.root:
            self.root.postorder()
        else:
            return False

    def remove(self, data):
        if not self.root:
            return False
        if self.root.value == data:
            if not self.root.leftchild and not self.root.rightchild:
                self.root = None
            elif self.root.leftchild and not self.root.rightchild:
                self.root = self.root.leftchild
            elif self.root.rightchild and not self.root.leftchild:
                self.root = self.root.rightchild
            elif self.root.leftchild and self.root.rightchild:
                delnodeparent = self.root
                delnode = self.root.rightchild
                while delnode.leftchild:
                    delnodeparent = delnode
                    delnode = delnode.leftchild
                self.root.value = delnode.value
                if delnode.rightchild:
                    
t = Tree()
t.insert(10)
t.insert(100)
t.insert(5)
print("preorder------>")
t.preorder()
print("inorder------>")
t.inorder()
print("postorder------>")
t.postorder()
