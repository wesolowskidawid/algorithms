import heapq
import sys


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))  # dla grafu nieskierowanego

    def dijkstra(self, source):
        dist = [float('inf')] * self.vertices
        dist[source] = 0
        priority_queue = [(0, source)]  # (odległość, wierzchołek)
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

            # Wizualizacja (drukowanie bieżącego stanu tablicy dist)
            print(f"Step: Visiting node {u}")
            print("Current distances:", dist)
            print("")

        return dist


# Funkcja pomocnicza do konwersji etykiet wierzchołków na indeksy
def vertex_label_to_index(label, vertex_mapping):
    return vertex_mapping[label]


# Przyklad użycia:
if __name__ == "__main__":
    # Tworzenie grafu
    vertex_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'J': 8}
    g = Graph(len(vertex_mapping))

    # Dodawanie krawędzi
    edges = [
        ('A', 'B', 0.7),
        ('A', 'C', 4.1),
        ('A', 'G', 3),
        ('B', 'C', 4),
        ('B', 'D', 1.2),
        ('B', 'E', 7.2),
        ('C', 'D', 2.1),
        ('C', 'F', 2.3),
        ('D', 'E', 4),
        ('D', 'F', 1),
        ('F', 'H', 1),
        ('H', 'G', 2.7),
        ('H', 'J', 4.9),
        ('J', 'G', 2.1)
    ]

    for u, v, weight in edges:
        g.add_edge(vertex_label_to_index(u, vertex_mapping), vertex_label_to_index(v, vertex_mapping), weight)

    source_label = 'A'
    source_index = vertex_label_to_index(source_label, vertex_mapping)
    shortest_distances = g.dijkstra(source_index)

    print("Shortest distances from source vertex", source_label)
    for label in vertex_mapping:
        index = vertex_label_to_index(label, vertex_mapping)
        print(f"To vertex {label}: {shortest_distances[index]}")
