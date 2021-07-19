"""
nodes/vertices and edges that connect them

networks in city, telephone, facebook etc

unweighted graph - no weight for edges
weighted graph - weight for edges (positive/negative)
undirected graph
directed graph
cyclic - leave on vertex and come back via some other path
acyclic
tree - directed acyclic

representation:
- adjacency matrix i.e. 2d table - for fuller graph - size cannot be changed
- adjacency list - vertices in array and edge in linked list - for sparsse graph - size can be changed
in python dict with key as vertex and value list as edges
"""

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addedge(self, vertex, edge):
        self.gdict[vertex].append(edge)

d = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": [],
    "d": [],
    "e": []
}

g = Graph(d)
print(g.gdict)
g.addedge("e", "c")
print(g.gdict)
