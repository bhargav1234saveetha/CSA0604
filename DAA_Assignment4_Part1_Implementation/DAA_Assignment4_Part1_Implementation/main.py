from fractional_knapsack import run as run_fractional
from job_sequencing import run as run_jobs
from knapsack01 import run as run_knapsack
from word_break import run as run_word_break
from shortest_paths import run as run_shortest_paths
from weighted_interval import run as run_weighted_interval

def main():
    tasks = [
        ("TASK 1 - FRACTIONAL KNAPSACK", run_fractional),
        ("TASK 2 - JOB SEQUENCING WITH DEADLINES", run_jobs),
        ("TASK 3 - 0/1 KNAPSACK USING DYNAMIC PROGRAMMING", run_knapsack),
        ("TASK 4 - WORD BREAK", run_word_break),
        ("TASK 5 - SHORTEST PATH ALGORITHMS", run_shortest_paths),
        ("TASK 6 - ENERGY-AWARE JOB SCHEDULING", run_weighted_interval),
    ]
    for title, function in tasks:
        print("\n" + "=" * 72)
        print(title)
        print("=" * 72)
        function()

if __name__ == "__main__":
    main()
