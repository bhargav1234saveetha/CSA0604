def fractional_knapsack(items, capacity):
    if capacity < 0 or any(w <= 0 for _, w, _ in items):
        raise ValueError("Capacity must be non-negative and weights positive")
    ordered = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    chosen, total = [], 0
    for name, weight, value in ordered:
        if capacity <= 0:
            break
        fraction = min(1, capacity / weight)
        chosen.append((name, fraction))
        total += fraction * value
        capacity -= fraction * weight
    return total, chosen

def zero_one_knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i, (_, weight, value) in enumerate(items, 1):
        for cap in range(capacity + 1):
            dp[i][cap] = dp[i - 1][cap]
            if weight <= cap:
                dp[i][cap] = max(dp[i][cap], value + dp[i - 1][cap - weight])
    chosen, cap = [], capacity
    for i in range(n, 0, -1):
        if dp[i][cap] != dp[i - 1][cap]:
            name, weight, _ = items[i - 1]
            chosen.append(name)
            cap -= weight
    return dp[n][capacity], list(reversed(chosen)), dp

def run():
    normal = [("A", 10, 60), ("B", 20, 100), ("C", 20, 100)]
    print("Normal fractional:", fractional_knapsack(normal, 50))
    print("Normal 0/1 DP:", zero_one_knapsack(normal, 50)[:2])
    items = [("A", 10, 60), ("B", 20, 100), ("C", 30, 120)]
    print("Counterexample fractional:", fractional_knapsack(items, 50))
    print("Counterexample 0/1 DP:", zero_one_knapsack(items, 50)[:2])
