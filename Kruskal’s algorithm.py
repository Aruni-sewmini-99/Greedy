
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    edges = []
    for v in graph:
        for u, weight in graph[v]:
            edges.append((weight, v, u))
    edges.sort()

    mst = []
    disjoint_set = DisjointSet(graph.keys())

    for weight, v1, v2 in edges:
        if disjoint_set.find(v1) != disjoint_set.find(v2):
            mst.append((v1, v2, weight))
            disjoint_set.union(v1, v2)

    return mst

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 2), ('D', 3)],
    'B': [('A', 2), ('C', 5), ('D', 1)],
    'C': [('B', 5), ('D', 4)],
    'D': [('A', 3), ('B', 1), ('C', 4)]
}

# Finding the MST using Kruskal's Algorithm
minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
