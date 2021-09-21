"""
properties:
- non linear
- hierarchical relationship
- no cycle
- every node has data and link to its subcategories
- base category has sub categories under it
- reverse of real tree

examples:
-         drinks
    hot           cold
tea    cofee   coke  pepsi
- folder structure
- org structure
- xml/html data

pros:
traversing linear structure takes more time with size increase

types:
- binary search tree performs fast search, insert, delete on sorted data
- AVL and red black tree have upperbound of O(n) for search

terminology:
- root - no parents
- edge - link between parent and child
- leaf - node that does not have children
- sibling - children of same parent
- ancestor - parent, grandparent, great grand parent etc of node
- depth of node - length from root to node
- height of node - length from this node to its deepest node
- depth of tree - depth of root node i.e. 0
- height of tree - height of root - length from root to deepest node
"""