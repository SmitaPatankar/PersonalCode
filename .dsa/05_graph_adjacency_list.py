# vertices and edges
# faster and less space for sparse graph

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        return False

    def print(self):
        for k, v in self.vertices.items():
            print(f"{k} --> {v.neighbors}")

g = Graph()
for i in "abcdefghijk":
    g.add_vertex(Vertex(i))

edges = ["ab", "ae", "bf", "cg", "de", "dh", "eh", "fg", "fi", "fj", "gj", "hi"]
for edge in edges:
    g.add_edge(edge[0], edge[1])

g.print()
