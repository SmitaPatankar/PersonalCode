class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            return False
        if self.data > data:
            if self.left:
                return self.left.insert(data)
            self.left = Node(data)
            return True
        if self.right:
            return self.right.insert(data)
        self.right = Node(data)
        return True

    def find(self, data):
        if self.data == data:
            return True
        if self.data > data:
            if self.left:
                return self.left.find(data)
            return False
        if self.right:
            return self.right.find(data)
        return False

    def preordertraversal(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preordertraversal()
        if self.right:
            self.right.preordertraversal()

    def postordertraversal(self):
        if self.left:
            self.left.postordertraversal()
        if self.right:
            self.right.postordertraversal()
        print(self.data, end=" ")

    def inordertraversal(self):
        if self.left:
            self.left.inordertraversal()
        print(self.data, end=" ")
        if self.right:
            self.right.inordertraversal()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preordertraversal(self):
        if self.root:
            self.root.preordertraversal()
            print()
        return False

    def postordertraversal(self):
        if self.root:
            self.root.postordertraversal()
            print()
        return False

    def inordertraversal(self):
        if self.root:
            self.root.inordertraversal()
            print()
        return False

    def remove(self, data):
        # empty tree
        if not self.root:
            return False

        # data to be deleted is in root
        if self.root.data == data:
            if not self.root.left and not self.root.right:
                self.root = None
            elif self.root.left and not self.root.right:
                self.root = self.root.left
            elif not self.root.left and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                delnode_parent = self.root
                delnode = self.root.right
                while delnode.left:
                    delnode_parent = delnode
                    delnode = delnode.left

                self.root.data = delnode.data
                if delnode.right:
                    if delnode.data < delnode_parent.data:
                        delnode_parent.left = delnode.right
                    elif delnode.data > delnode_parent.data:
                        delnode_parent.right = delnode.right
                else:
                    if delnode.data < delnode_parent.data:
                        delnode_parent.left = None
                    else:
                        delnode_parent.right = None

            return True

        parent = None
        node = self.root

        while node and node.data != data:
            parent = node
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right

        # case 1: data not found
        if not node or node.data != data:
            return False

        # case 2: remove-node has no children
        elif not node.left and not node.right:
            if data < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True

        # case 3: remove-node has left child only
        elif node.left and not node.right:
            if data < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        # case 4: remove-node has right child only
        elif not node.left and node.right:
            if data < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        # case 5: remove-node has left and right children
        else:
            delnode_parent = node
            delnode = node.right
            while delnode.left:
                delnode_parent = delnode
                delnode = delnode.left

            node.data = delnode.data
            if delnode.right:
                if delnode.data < delnode_parent.data:
                    delnode_parent.left = delnode.right
                elif delnode_parent.data < delnode.data:
                    delnode_parent.right = delnode.right
            else:
                if delnode.data < delnode_parent.data:
                    delnode_parent.left = None
                else:
                    delnode_parent.right = None


print("creating tree")
t = Tree()

print("inorder traversal")
t.inordertraversal()

print("inserting elements")
t.insert(10)
t.insert(5)
t.insert(30)
t.insert(100)
t.insert(2)

print("preorder traversal")
t.preordertraversal()

print("inorder traversal")
t.inordertraversal()

print("postorder traversal")
t.postordertraversal()

print("finding element")
print(t.find(5))

print("finding incorrect element")
print(t.find(500))

print("removing element")
t.remove(5)

print("inorder traversal")
t.inordertraversal()

print("removing incorrect element")
t.remove(1000)

print("inorder traversal")
t.inordertraversal()
