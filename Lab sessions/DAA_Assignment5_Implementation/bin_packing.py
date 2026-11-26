def first_fit_decreasing(workloads, capacity):
    """Pack workloads using First-Fit Decreasing."""
    if capacity <= 0:
        raise ValueError("Server capacity must be positive")

    for item in workloads:
        if item < 0 or item > capacity:
            raise ValueError("Each workload must be between 0 and capacity")

    items = sorted(workloads, reverse=True)
    servers = []

    for item in items:
        placed = False

        for server in servers:
            if sum(server) + item <= capacity:
                server.append(item)
                placed = True
                break

        if not placed:
            servers.append([item])

    return servers


def print_packing(workloads, capacity):
    servers = first_fit_decreasing(workloads, capacity)

    print("Workloads:", workloads)
    print("Capacity per server:", capacity)
    print("Servers used:", len(servers))

    for index, server in enumerate(servers, 1):
        print(
            f"Server {index}: workloads={server}, "
            f"used={sum(server)}, remaining={capacity - sum(server)}"
        )


def run_bin_packing_demo():
    print_packing([8, 7, 6, 5, 4, 3, 2, 2, 1], 10)

    print("\nBoundary test - exact capacity workload")
    print_packing([10], 10)

    print("\nValidation test - oversized workload")
    try:
        first_fit_decreasing([12, 4], 10)
    except ValueError as error:
        print("Expected validation message:", error)
