def dijkstra(graph, source):
    if source not in graph:
        raise ValueError("Source vertex is not in graph")
    if any(weight < 0 for edges in graph.values() for _, weight in edges):
        raise ValueError("Dijkstra requires non-negative edge weights")

    distance = {vertex: float("inf") for vertex in graph}
    predecessor = {vertex: None for vertex in graph}
    visited = set()
    final_order = []
    distance[source] = 0

    while True:
        candidates = [v for v in graph if v not in visited]
        if not candidates:
            break
        u = min(candidates, key=lambda vertex: distance[vertex])
        if distance[u] == float("inf"):
            break

        visited.add(u)
        final_order.append(u)

        for v, weight in graph[u]:
            if v not in visited and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u

    return distance, predecessor, final_order


def bellman_ford(vertices, edges, source):
    distance = {v: float("inf") for v in vertices}
    predecessor = {v: None for v in vertices}
    distance[source] = 0

    for _ in range(len(vertices) - 1):
        changed = False
        for u, v, weight in edges:
            if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u
                changed = True
        if not changed:
            break

    for u, v, weight in edges:
        if distance[u] != float("inf") and distance[u] + weight < distance[v]:
            return distance, predecessor, True

    return distance, predecessor, False


def reconstruct_path(predecessor, target):
    path = []
    while target is not None:
        path.append(target)
        target = predecessor[target]
    return list(reversed(path))


def floyd_warshall(vertices, edges):
    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    distance = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        distance[i][i] = 0
    for u, v, weight in edges:
        i, j = index[u], index[v]
        distance[i][j] = min(distance[i][j], weight)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] != float("inf") and distance[k][j] != float("inf"):
                    distance[i][j] = min(
                        distance[i][j],
                        distance[i][k] + distance[k][j]
                    )
    return distance


def run():
    vertices = list("ABCDE")
    edges = [
        ("A", "B", 4), ("A", "C", 7), ("B", "C", 2),
        ("B", "D", 6), ("C", "D", 1), ("D", "E", 3),
        ("C", "E", 8)
    ]
    graph = {v: [] for v in vertices}
    for u, v, weight in edges:
        graph[u].append((v, weight))

    distance, predecessor, order = dijkstra(graph, "A")
    print("Dijkstra distances:", distance)
    print("Predecessors:", predecessor)
    print("Finalisation order:", order)
    print("Shortest path A to E:", reconstruct_path(predecessor, "E"))

    negative_edge = edges + [("E", "B", -1)]
    bf_distance, _, has_cycle = bellman_ford(vertices, negative_edge, "A")
    print("\nBellman-Ford with negative edge E->B (-1)")
    print("Reachable negative cycle:", has_cycle)
    print("Distances:", bf_distance)

    negative_cycle = edges + [("E", "B", -5)]
    _, _, has_cycle = bellman_ford(vertices, negative_cycle, "A")
    print("With E->B (-5), reachable negative cycle:", has_cycle)

    matrix = floyd_warshall(vertices, edges)
    print("\nFloyd-Warshall all-pairs distance matrix:")
    print("   ", *vertices)
    for vertex, row in zip(vertices, matrix):
        print(vertex, *[("INF" if x == float("inf") else x) for x in row])
