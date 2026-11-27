def knapsack01(items, capacity):
    """
    items: list of (item_id, weight, value)
    Returns optimum value, selected item IDs and DP table.
    """
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")
    if any(weight < 0 for _, weight, _ in items):
        raise ValueError("Weights cannot be negative")

    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i, (name, weight, value) in enumerate(items, 1):
        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]
            if weight <= current_capacity:
                include = value + dp[i - 1][current_capacity - weight]
                dp[i][current_capacity] = max(
                    dp[i][current_capacity], include
                )

    selected = []
    current_capacity = capacity
    for i in range(n, 0, -1):
        if dp[i][current_capacity] != dp[i - 1][current_capacity]:
            name, weight, value = items[i - 1]
            selected.append(name)
            current_capacity -= weight

    selected.reverse()
    return dp[n][capacity], selected, dp


def run():
    items = [
        ("P", 2, 12),
        ("Q", 3, 20),
        ("R", 4, 25),
        ("S", 5, 30)
    ]
    capacity = 7
    value, selected, table = knapsack01(items, capacity)
    print("Items (ID, weight, value):", items)
    print("Capacity:", capacity)
    print("Maximum value:", value)
    print("Selected items:", selected)
    print("DP table:")
    for row in table:
        print(row)
    print("Selected total weight:",
          sum(weight for name, weight, val in items if name in selected))

    print("\nBoundary test - zero capacity:")
    print(knapsack01(items, 0)[:2])
