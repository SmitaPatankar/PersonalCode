"""
parent action -> dependent action
many ways

if a vertex depends on current vertex, go there and come back
else push current vertex to stack
pop stack at end

O(E+V), O(E+V)
"""

from collections import defaultdict

class Graph:
    def __init__(self, noofvertices):
        self.graph = defaultdict(list)
        self.noofvertices = noofvertices

    def addedge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalsortutil(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalsortutil(i, visited, stack)
        stack.insert(0,v)

    def topologicalsort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalsortutil(k, visited, stack)
        print(stack)

g = Graph(8)
g.addedge("a", "c")
g.addedge("c", "e")
g.addedge("e", "h")
g.addedge("e", "f")
g.addedge("f", "g")
g.addedge("b", "h")
g.addedge("e", "h")
g.addedge("d", "f")
g.topologicalsort()
