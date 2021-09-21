"""
breadth first search
explore neighbors before exploring next level of neighbors like level order
enqueue root
while:
    dequeue queue
    if unvisited:
        mark visited
        enqueue unvisited linked vertices
O(V+E), O(V+E)

depth first search
take a vertex and explore its edges as far as possible before backtracking
push start vertex to stack
while stack:
    pop
    mark visited
    push adjacent vertices
O(V+E), O(V+E)

bfs vs dfs
bfs - if we know target is close to starting point
dfs - if we know target is deep
"""

class Graph:
    def __init__(self, gdict=None):
        if not gdict:
            gdict = {}
        self.gdict = gdict

    def addedge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queueu = [vertex]
        while queueu:
            devertex = queueu.pop(0)
            print(devertex)
            for adjvertex in self.gdict[devertex]:
                if adjvertex not in visited:
                    visited.append(adjvertex)
                    queueu.append(adjvertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            devertex = stack.pop()
            print(devertex)
            for adjvertex in self.gdict[devertex]:
                if adjvertex not in visited:
                    visited.append(adjvertex)
                    stack.append(adjvertex)

d = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"]
}
g = Graph(d)
g.bfs("a")
print("###########")
g.dfs("a")
