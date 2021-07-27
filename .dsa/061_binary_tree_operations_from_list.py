"""
leftchild = 2x
rightchild = 2x + 1
x = node location
skip using 0
root is at 1

create:
    fixed size list
    last used index set to 0
insert:(if not full)
    first vacant place
search:
    level order traversal
traverse:(4 ways)
    recursive functions as per 2x and 2x+1
delete:
    find deepest node
    replace node with deepest node
    delete deepest node
"""

class Tree:
    # O(1), O(n)
    def __init__(self, size):
        self.list = size * [None]
        self.maxsize = size
        self.lastusedindex = 0

    # O(1), O(1)
    def insert(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return "full"
        self.list[self.lastusedindex + 1] = value
        self.lastusedindex += 1
        return "inserted"

    # O(n), O(1)
    def search(self, value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                return value
        return "not found"

    # O(n), O(n)
    def preordertraversal(self, index):
        if index > self.lastusedindex:
            return
        print(self.list[index])
        self.preordertraversal(index*2)
        self.preordertraversal(index*2 + 1)

    # O(n), O(n)
    def inordertraversal(self, index):
        if index > self.lastusedindex:
            return
        self.inordertraversal(index*2)
        print(self.list[index])
        self.inordertraversal(index*2 + 1)

    # O(n), O(n)
    def postordertraversal(self, index):
        if index > self.lastusedindex:
            return
        self.postordertraversal(index*2)
        self.postordertraversal(index*2 + 1)
        print(self.list[index])

    # O(n), O(1)
    def levelordertraversal(self, index):
        for i in range(index, self.lastusedindex+1):
            print(self.list[i])

    # O(n), O(1)
    def delete(self, value):
        if self.lastusedindex == 0:
            return "empty"
        for i in range(1, self.lastusedindex+1):
            if self.list[i] == value:
                self.list[i] = self.list[self.lastusedindex]
                self.list[self.lastusedindex] = None
                self.lastusedindex -= 1
                return "deleted"
        return "failed to delete"

    # O(1), O(1)
    def delete_entire(self):
        self.list = None
        print("deleted")

t = Tree(8)
print(t.insert("drinks"))
print(t.insert("hot"))
print(t.insert("cold"))
print(t.insert("tea"))
print(t.insert("coffee"))
print("#######")
print(t.search("hot"))
print(t.search("blah"))
print("#######")
t.preordertraversal(1)
print("#######")
t.inordertraversal(1)
print("#######")
t.postordertraversal(1)
print("#######")
t.levelordertraversal(1)
print("#######")
print(t.delete("tea"))
t.levelordertraversal(1)
print("#######")
print(t.delete_entire())
