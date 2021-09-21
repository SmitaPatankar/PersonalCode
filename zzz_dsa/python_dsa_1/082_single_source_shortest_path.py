"""
min distance between source and destination

BFS
keep track of parent each time
enqueue a vertex
while queueu:
    dequeue
    if unvisited:
        enqueue adj vertices
        update parent of adj vertices to current

Dijkstra's algorithm
bellman ford

no DFS because it shows longest path


time
bfs, dijkstra - O(V^2)
bellman ford - O(VE)

space
cfs - o(e)
dijskstra, bell - o(v)

easy, moderate, moderate
"""