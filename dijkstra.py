import heapq
import sys


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))  # for undirected graph

    def dijkstra(self, source, index_to_label):
        dist = [float('inf')] * self.vertices
        dist[source] = 0
        priority_queue = [(0, source)]  # (distance, vertex)
        visited = set()

        while priority_queue:
            current_dist, u = heapq.heappop(priority_queue)

            if u in visited:
                continue

            visited.add(u)

            for v, weight in self.adjacency_list[u]:
                if v not in visited:
                    new_dist = current_dist + weight
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(priority_queue, (new_dist, v))

            # Visualization (printing current state of dist array)
            print(f"Step: Visiting node {index_to_label[u]}")
            print("Current distances:", {index_to_label[i]: d for i, d in enumerate(dist)})
            print("")

        return dist


# Helper function to convert vertex labels to indices
def vertex_label_to_index(label, vertex_mapping):
    return vertex_mapping[label]


# Example usage:
if __name__ == "__main__":
    # Creating the graph
    vertex_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'J': 8}
    index_to_label = {v: k for k, v in vertex_mapping.items()}
    g = Graph(len(vertex_mapping))

    # Adding edges
    edges = [
        ('A', 'B', 1.3),
        ('A', 'E', 4),
        ('A', 'H', 0.5),
        ('B', 'E', 1.2),
        ('B', 'C', 0.7),
        ('B', 'D', 2.4),
        ('B', 'E', 1.2),
        ('C', 'D', 0.4),
        ('C', 'F', 3),
        ('D', 'E', 0.1),
        ('D', 'H', 2.3),
        ('D', 'G', 1),
        ('E', 'H', 1.3),
        ('G', 'H', 1),
        ('F', 'G', 0.7),
        ('F', 'J', 2.1),
        ('G', 'J', 4.9),
    ]

    for u, v, weight in edges:
        g.add_edge(vertex_label_to_index(u, vertex_mapping), vertex_label_to_index(v, vertex_mapping), weight)

    source_label = 'A'
    source_index = vertex_label_to_index(source_label, vertex_mapping)
    shortest_distances = g.dijkstra(source_index, index_to_label)

    print("Shortest distances from source vertex", source_label)
    for label in vertex_mapping:
        index = vertex_label_to_index(label, vertex_mapping)
        print(f"To vertex {label}: {shortest_distances[index]}")
