from graph_coloring import run_graph_coloring_demo
from set_cover import run_set_cover_demo
from bin_packing import run_bin_packing_demo

def main():
    print("=" * 60)
    print("DAA ASSIGNMENT 5 - IMPLEMENTATION")
    print("=" * 60)

    print("\n[B1 and B2] GRAPH COLOURING")
    run_graph_coloring_demo()

    print("\n[B3] EXACT VS GREEDY SET COVER")
    run_set_cover_demo()

    print("\n[B4] BIN PACKING - FIRST FIT DECREASING")
    run_bin_packing_demo()

if __name__ == "__main__":
    main()
