import heapq
import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))  # for undirected graph

    def dijkstra(self, source):
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

            # Visualization (print current state of dist array)
            print(f"Step: Visiting node {u}")
            print("Current distances:", dist)
            print("")

        return dist

# Example usage:
if __name__ == "__main__":
    # Example graph
    g = Graph(5)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 4, 1)

    source = 0
    shortest_distances = g.dijkstra(source)
    print("Shortest distances from source vertex", source)
    for i in range(len(shortest_distances)):
        print(f"To vertex {i}: {shortest_distances[i]}")
