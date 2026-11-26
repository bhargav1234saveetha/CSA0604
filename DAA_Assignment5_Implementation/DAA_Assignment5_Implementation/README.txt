DAA ASSIGNMENT 5 - IMPLEMENTATION FOLDER
========================================

CONTENTS
--------
main.py
    Runs all implementation tasks.

graph_coloring.py
    B1: Backtracking graph colouring.
    Records search nodes, candidate attempts, rejected branches,
    backtracks and maximum depth.
    Compares input order with descending-degree heuristic.
    Includes colourable, uncolourable, boundary and B2 adversarial tests.

set_cover.py
    B3: Exact minimum set cover and greedy set cover.
    Includes three test cases, the assignment's greedy counterexample,
    and a small scalability investigation.
    Counts exact subsets checked and greedy gain evaluations.

bin_packing.py
    B4: First-Fit Decreasing bin-packing heuristic.
    Prints server assignments and remaining capacity.
    Includes boundary and invalid-input tests.

HOW TO RUN
----------
1. Install Python 3 if it is not already installed.
2. Extract this folder.
3. Open the folder in VS Code.
4. Open the terminal in VS Code.
5. Run:

       python main.py

No external Python packages are required.

IMPORTANT
---------
Run the program on your own computer and use the actual output produced
there in your assignment report. Search counters can depend on vertex
ordering and implementation details. Explain the results in your own words.

This folder implements Part B (B1-B4) of Assignment 5. Part A requires
language-independent pseudocode and written explanations, not Python code.
