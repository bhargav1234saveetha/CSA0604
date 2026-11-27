def weighted_interval_scheduling(jobs):
    """
    jobs: list of (job_id, start, finish, value)
    Returns selected compatible jobs, maximum value and DP array.
    """
    ordered = sorted(jobs, key=lambda job: job[2])
    n = len(ordered)
    previous = [0] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if ordered[j][2] <= ordered[i][1]:
                previous[i] = j + 1
                break

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        include = ordered[i - 1][3] + dp[previous[i - 1]]
        exclude = dp[i - 1]
        dp[i] = max(include, exclude)

    selected = []
    i = n
    while i > 0:
        include = ordered[i - 1][3] + dp[previous[i - 1]]
        if include > dp[i - 1]:
            selected.append(ordered[i - 1])
            i = previous[i - 1]
        else:
            i -= 1

    selected.reverse()
    return selected, dp[n], dp, ordered, previous


def run():
    jobs = [
        ("J1", 1, 3, 20),
        ("J2", 2, 5, 50),
        ("J3", 4, 6, 30),
        ("J4", 6, 8, 40),
        ("J5", 5, 9, 60),
        ("J6", 8, 10, 30),
        ("J7", 9, 11, 50),
        ("J8", 11, 13, 40)
    ]
    selected, total, dp, ordered, previous = weighted_interval_scheduling(jobs)
    print("Jobs sorted by finish time:", ordered)
    print("Previous compatible indices (1-based DP positions):", previous)
    print("DP values:", dp)
    print("Selected jobs:", selected)
    print("Maximum energy saving:", total)

    adversarial = [
        ("A", 1, 2, 20),
        ("B", 1, 10, 100),
        ("C", 2, 4, 20),
        ("D", 4, 6, 20),
        ("E", 6, 8, 20)
    ]
    result = weighted_interval_scheduling(adversarial)
    print("\nAdversarial test - several short jobs vs one long job:")
    print("Selected jobs:", result[0])
    print("Maximum value:", result[1])
