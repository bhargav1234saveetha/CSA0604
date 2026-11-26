from itertools import combinations


def exact_cover(universe, centres):
    """Return a minimum-cardinality cover and number of subsets checked."""
    names = list(centres)
    checks = 0

    for size in range(1, len(names) + 1):
        for group in combinations(names, size):
            checks += 1
            covered = set()
            for name in group:
                covered.update(centres[name])

            if covered >= universe:
                return list(group), checks

    return None, checks


def greedy_cover(universe, centres):
    """Return a greedy cover and number of centre-gain evaluations."""
    uncovered = set(universe)
    selected = []
    evaluations = 0

    while uncovered:
        best_name = None
        best_gain = set()

        for name, zones in centres.items():
            if name in selected:
                continue

            evaluations += 1
            gain = zones & uncovered

            if len(gain) > len(best_gain):
                best_name = name
                best_gain = gain

        if best_name is None or not best_gain:
            return None, evaluations

        selected.append(best_name)
        uncovered -= best_gain

    return selected, evaluations


def show_case(title, centres):
    universe = set()
    for zones in centres.values():
        universe.update(zones)

    exact, checks = exact_cover(universe, centres)
    greedy, evaluations = greedy_cover(universe, centres)

    print(f"\n{title}")
    print("Universe:", sorted(universe))
    print("Centres:", centres)
    print("Exact cover:", exact, "| size:", len(exact) if exact else None)
    print("Exact subsets checked:", checks)
    print("Greedy cover:", greedy, "| size:", len(greedy) if greedy else None)
    print("Greedy gain evaluations:", evaluations)


def run_set_cover_demo():
    cases = [
        {
            "A": {1, 2, 3}, "B": {4, 5}, "C": {6},
            "D": {1, 4}, "E": {2, 5, 6}
        },
        {
            "A": {1, 2}, "B": {3, 4},
            "C": {1, 3}, "D": {2, 4}
        },
        {
            "A": {1, 2, 3, 4}, "B": {5, 6},
            "C": {1, 5}, "D": {2, 6}, "E": {3, 4}
        }
    ]

    for i, centres in enumerate(cases, 1):
        show_case(f"Test case {i}", centres)

    # Greedy counterexample from the assignment
    counterexample = {
        "A": {1, 2, 3, 4},
        "B": {1, 2, 5},
        "C": {3, 4, 6},
        "D": {5},
        "E": {6}
    }
    show_case("Greedy counterexample", counterexample)

    # Increasing input sizes: deterministic generated instances
    print("\nScalability investigation")
    for count in [5, 8, 10, 12]:
        centres = {}
        universe = set(range(1, count + 1))
        for i in range(count):
            centres[f"C{i + 1}"] = {i + 1, ((i + 1) % count) + 1}
        exact, checks = exact_cover(universe, centres)
        greedy, evaluations = greedy_cover(universe, centres)
        print(
            f"{count} zones / {count} centres: "
            f"exact_size={len(exact) if exact else None}, "
            f"subsets_checked={checks}, "
            f"greedy_size={len(greedy) if greedy else None}, "
            f"greedy_evaluations={evaluations}"
        )
