def fractional_knapsack(items, capacity):
    """
    items: list of (item_id, weight, value)
    Returns maximum value and selected fractions.
    """
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")
    if any(weight <= 0 for _, weight, _ in items):
        raise ValueError("Every item weight must be positive")

    ordered = sorted(items, key=lambda item: item[2] / item[1], reverse=True)
    remaining = capacity
    total_value = 0.0
    selected = []

    for name, weight, value in ordered:
        if remaining == 0:
            break
        fraction = min(1.0, remaining / weight)
        selected.append((name, fraction))
        total_value += fraction * value
        remaining -= fraction * weight

    return total_value, selected


def run():
    items = [("A", 10, 60), ("B", 20, 100), ("C", 30, 120)]
    capacity = 50
    value, selected = fractional_knapsack(items, capacity)
    print("Items (ID, weight, value):", items)
    print("Capacity:", capacity)
    print("Selected fractions:", selected)
    print("Maximum value:", value)

    print("\nBoundary test - zero capacity:")
    print(fractional_knapsack(items, 0))

    print("\nValidation test - zero weight:")
    try:
        fractional_knapsack([("X", 0, 10)], 10)
    except ValueError as error:
        print("Expected validation:", error)
