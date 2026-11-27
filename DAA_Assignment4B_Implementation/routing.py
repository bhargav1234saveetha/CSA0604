import heapq

def dijkstra(graph, source):
    if any(w < 0 for edges in graph.values() for _, w in edges):
        raise ValueError("Dijkstra requires non-negative weights")
    dist = {v: float("inf") for v in graph}
    prev = {v: None for v in graph}
    order, dist[source], queue = [], 0, [(0, source)]
    while queue:
        d, u = heapq.heappop(queue)
        if d != dist[u]:
            continue
        order.append(u)
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v], prev[v] = d + w, u
                heapq.heappush(queue, (dist[v], v))
    return dist, prev, order

def path(prev, target):
    result = []
    while target is not None:
        result.append(target)
        target = prev[target]
    return list(reversed(result))

def bellman_ford(vertices, edges, source):
    dist, prev = {v: float("inf") for v in vertices}, {v: None for v in vertices}
    dist[source] = 0
    for _ in range(len(vertices) - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v], prev[v], changed = dist[u] + w, u, True
        if not changed:
            break
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            return dist, prev, True
    return dist, prev, False

def floyd_warshall(vertices, edges):
    n, ix = len(vertices), {v: i for i, v in enumerate(vertices)}
    d = [[float("inf")] * n for _ in range(n)]
    for i in range(n): d[i][i] = 0
    for u, v, w in edges: d[ix[u]][ix[v]] = min(d[ix[u]][ix[v]], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] != float("inf") and d[k][j] != float("inf"):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def warshall(vertices, edges):
    n, ix = len(vertices), {v: i for i, v in enumerate(vertices)}
    r = [[False] * n for _ in range(n)]
    for i in range(n): r[i][i] = True
    for u, v, _ in edges: r[ix[u]][ix[v]] = True
    for k in range(n):
        for i in range(n):
            for j in range(n): r[i][j] = r[i][j] or (r[i][k] and r[k][j])
    return r

def run():
    vs = list("ABCDEFGH")
    es = [("A","B",4),("A","C",8),("B","C",2),("B","D",5),
          ("C","D",1),("C","E",7),("D","E",3),("D","F",6),
          ("E","F",2),("F","G",3),("G","H",2),("E","H",8),
          ("B","G",10),("A","H",20)]
    graph = {v: [] for v in vs}
    for u, v, w in es: graph[u].append((v, w))
    dist, prev, order = dijkstra(graph, "A")
    print("Dijkstra distances:", dist)
    print("Predecessors:", prev, "Finalisation order:", order)
    print("Path A to H:", path(prev, "H"))
    d, _, cycle = bellman_ford(vs, es + [("H","D",-8)], "A")
    print("Bellman-Ford with H->D -8; negative cycle:", cycle, "distances:", d)
    _, _, cycle = bellman_ford(vs, es + [("H","D",-12)], "A")
    print("With H->D -12, reachable negative cycle:", cycle)
    for title, matrix in [("Floyd distance matrix", floyd_warshall(vs, es)),
                          ("Warshall reachability matrix", warshall(vs, es))]:
        print(title)
        print("   ", *vs)
        for v, row in zip(vs, matrix): print(v, *row)
