
import heapq


def prim(graph):
    # Initialize an empty set to store visited vertices
    visited = set()

    # Initialize a priority queue to store edges
    pq = []

    # Start from vertex 0
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)

    # Add all edges connected to start_vertex to the priority queue
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(pq, (weight, start_vertex, neighbor))

    # Initialize the minimum spanning tree
    mst = []

    # Loop until all vertices are visited
    while pq:
        weight, u, v = heapq.heappop(pq)

        # If v is not visited yet, add the edge to the MST
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            # Add all edges connected to v to the priority queue
            for neighbor, weight in graph[v]:
                heapq.heappush(pq, (weight, v, neighbor))

    return mst


# Example graph represented as an adjacency list
graph = {
    'A': [('B', 2), ('D', 3)],
    'B': [('A', 2), ('C', 5), ('D', 1)],
    'C': [('B', 5), ('D', 4)],
    'D': [('A', 3), ('B', 1), ('C', 4)]
}

# Finding the MST using Prim's Algorithm
minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
