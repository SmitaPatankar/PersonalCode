"""
search string in space and time efficient way
node has nonrepetitive multiple characters
node has link to next character
node has track of end of string

spelling checker
auto complete

create
insert
    blank trie
    prefix already exists
    prefix already exists as complete string
    complete string exists  
search
    doesnt exist
    exists
    only prefix exists
delete from bottom
    prefix is shared
    complete string is shared
    other string is prefix
    no dependency
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstring = False

class Trie:
    # O(1), O(1)
    def __init__(self):
        self.root = TrieNode()

    # O(m), O(m) - no of chars in word
    def insertstring(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endofstring = True
        print("inserted")

    # O(m), O(1)
    def search(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if not node:
                return
            current = node
        if current. endofstring == True:
            print("found")

# learn more - write on own - understand
def delete(root, word, index):
    ch = word[index]
    currentnode = root.children.get(ch)
    canthisbedeleted = False
    if len(currentnode.children) > 1:
        delete(currentnode, word, index+1)
        return False
    if index == len(word) - 1:
        if len(currentnode.children) >= 1:
            currentnode.endofstring = False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentnode.endofstring == True:
        delete(currentnode, word, index+1)
        return False
    canthisbedeleted = delete(currentnode, word, index+1)
    if canthisbedeleted:
        root.children.pop(ch)
        return True
    else:
        return False

newtrie = Trie()
newtrie.insertstring("app")
newtrie.insertstring("api")
newtrie.search("api")
delete(newtrie.root, "api", 0)
print("#########")
newtrie.search("api")
print("#########")
newtrie.search("app")
