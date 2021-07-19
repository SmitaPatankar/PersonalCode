"""
O(E), O(E)

only for unweighted graphs
as less weight can be for some other path also, which is not breadth first
"""

class Graph:
    def __init__(self, gdict=None):
        if not gdict:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = []
        queue.append(start)
        while queue:
            path = queue.pop(0)
            node = path[-1]  
            if node == end:
                return path
            for adj in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)

d = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["e"]
}
g = Graph(d)
print(g.bfs("a", "f"))
