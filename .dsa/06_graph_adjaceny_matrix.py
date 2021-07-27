# vertices and edges
# faster for dense
# simpler for weighted graph
# more space

class Vertex:
    def __init__(self, name):
        self.name = name

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            ui = self.edge_indices[u]
            vi = self.edge_indices[v]
            self.edges[ui][vi] = weight
            self.edges[vi][ui] = weight
            return True
        return False

    def print(self):
        print("\t", end="")
        print("\t".join(self.vertices))
        for v, i in self.edge_indices.items():
            print(v, end="\t")
            for j in range(len(self.edges)):
                print(self.edges[i][j], end = "\t")
            print("")

g = Graph()
for i in "abcdefghijk":
    g.add_vertex(Vertex(i))

edges = ["ab", "ae", "bf", "cg", "de", "dh", "eh", "fg", "fi", "fj", "gj", "hi"]
for edge in edges:
    g.add_edge(edge[0], edge[1])

g.print()
