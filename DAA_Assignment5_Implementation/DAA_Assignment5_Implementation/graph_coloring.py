def colour_graph(vertices, edges, k, heuristic=False):
    """Backtracking graph colouring with search instrumentation."""
    adj = {v: set() for v in vertices}

    for u, v in edges:
        if u not in adj or v not in adj:
            raise ValueError("Every edge endpoint must be in vertices")
        adj[u].add(v)
        adj[v].add(u)

    order = list(vertices)
    if heuristic:
        order.sort(key=lambda v: len(adj[v]), reverse=True)

    colours = {v: 0 for v in vertices}
    stats = {
        "nodes": 0,
        "attempts": 0,
        "rejected": 0,
        "backtracks": 0,
        "max_depth": 0
    }

    def search(index):
        stats["nodes"] += 1
        stats["max_depth"] = max(stats["max_depth"], index)

        if index == len(order):
            return True

        vertex = order[index]

        for colour in range(1, k + 1):
            stats["attempts"] += 1

            if all(colours[n] != colour for n in adj[vertex]):
                colours[vertex] = colour

                if search(index + 1):
                    return True

                colours[vertex] = 0
                stats["backtracks"] += 1
            else:
                stats["rejected"] += 1

        return False

    success = search(0)
    return success, colours if success else None, stats


def make_complete_graph(vertices):
    edges = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            edges.append((vertices[i], vertices[j]))
    return edges


def print_result(name, result):
    success, colouring, stats = result
    print(f"\n{name}")
    print("Colourable:", success)
    print("Colour assignment:", colouring)
    print("Search statistics:", stats)


def run_graph_coloring_demo():
    vertices = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "B"), ("A", "C"), ("B", "C"),
        ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")
    ]

    print_result("Example graph - input order",
                 colour_graph(vertices, edges, 3))
    print_result("Example graph - degree heuristic",
                 colour_graph(vertices, edges, 3, heuristic=True))

    # Boundary test: empty graph
    print_result("Boundary test - empty graph",
                 colour_graph([], [], 3))

    # Uncolourable test: complete graph K4 with only 3 colours
    k4_vertices = [1, 2, 3, 4]
    k4_edges = make_complete_graph(k4_vertices)
    print_result("Uncolourable test - K4 with 3 colours",
                 colour_graph(k4_vertices, k4_edges, 3))

    # Adversarial comparison: path versus complete graph K6
    six = [1, 2, 3, 4, 5, 6]
    path_edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    complete_edges = make_complete_graph(six)

    print_result("B2 Graph A - path with 6 vertices",
                 colour_graph(six, path_edges, 3))
    print_result("B2 Graph B - K6 with 3 colours",
                 colour_graph(six, complete_edges, 3))
