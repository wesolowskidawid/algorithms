# Funkcja szukająca cykl Eulera w grafie
def find_eulerian_cycle(graph):
    # Sprawdzenie czy każdy wierzchołek ma parzysty stopień
    # Jeżeli nie, to cykl Eulera nie istnieje
    for vertex in graph:
        if len(graph[vertex]) % 2 != 0:
            return None

    # Inicjalizacja stosu i ścieżki
    stack = []
    eulerian_cycle = []

    # Wybieramy dowolny wierzchołek jako startowy
    current_vertex = next(iter(graph))

    while True:
        # Dopóki istnieją krawędzie w grafie
        if graph[current_vertex]:
            # Dodajemy bieżący wierzchołek na stos
            stack.append(current_vertex)
            # Wybieramy dowolny sąsiadni wierzchołek
            next_vertex = graph[current_vertex].pop()
            # Usuwamy odpowiednią krawędź z grafu
            graph[next_vertex].remove(current_vertex)
            # Przechodzimy do wybranego sąsiada
            current_vertex = next_vertex
        else:
            # Jeśli brak sąsiadów, dodajemy bieżący wierzchołek do cyklu Eulera
            eulerian_cycle.append(current_vertex)
            # Jeśli stos jest pusty, kończymy
            if not stack:
                break
            # Pobieramy wierzchołek ze stosu jako bieżący wierzchołek
            current_vertex = stack.pop()

    return eulerian_cycle

if __name__ == '__main__':
    # Przykład grafu z cyklem Eulera
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }

    cycle = find_eulerian_cycle(graph)
    if cycle:
        print('Cykl Eulera:', cycle)
    else:
        print('Cykl Eulera nie istnieje')
