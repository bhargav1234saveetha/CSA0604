from word_wrap import run
from knapsack import run as run_knapsack
from routing import run as run_routing
from assembly_line import run as run_assembly
from mst import run as run_mst
from tsp import run as run_tsp

if __name__ == "__main__":
    for title, function in [
        ("TASK 1 - WORD WRAP", run),
        ("TASK 2 - KNAPSACK", run_knapsack),
        ("TASK 3 - SHORTEST PATHS", run_routing),
        ("TASK 4 - ASSEMBLY LINE", run_assembly),
        ("TASK 5 - MINIMUM SPANNING TREE", run_mst),
        ("TASK 6 - TSP", run_tsp),
    ]:
        print("\n" + "=" * 65 + "\n" + title)
        function()
