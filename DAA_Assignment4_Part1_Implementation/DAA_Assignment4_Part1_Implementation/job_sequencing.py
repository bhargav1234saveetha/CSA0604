def job_sequencing(jobs):
    """
    jobs: list of (job_id, deadline, profit)
    Each job takes one slot. Returns slot schedule and total profit.
    """
    if any(deadline < 0 for _, deadline, _ in jobs):
        raise ValueError("Deadlines cannot be negative")

    if not jobs:
        return [], 0

    ordered = sorted(jobs, key=lambda job: job[2], reverse=True)
    max_deadline = max(deadline for _, deadline, _ in jobs)
    schedule = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in ordered:
        slot = min(deadline, max_deadline) - 1
        while slot >= 0 and schedule[slot] is not None:
            slot -= 1

        if slot >= 0:
            schedule[slot] = job_id
            total_profit += profit

    return schedule, total_profit


def run():
    jobs = [
        ("A", 2, 80),
        ("B", 1, 35),
        ("C", 2, 60),
        ("D", 3, 40),
        ("E", 1, 25)
    ]
    schedule, profit = job_sequencing(jobs)
    print("Jobs (ID, deadline, profit):", jobs)
    print("Final schedule:")
    for slot, job in enumerate(schedule, 1):
        print(f"Slot {slot}: {job if job is not None else 'EMPTY'}")
    print("Maximum profit:", profit)

    changed = [(name, deadline, 90 if name == "D" else value)
               for name, deadline, value in jobs]
    print("\nChanged D profit to 90:")
    print(job_sequencing(changed))

    print("\nBoundary test - no jobs:")
    print(job_sequencing([]))
