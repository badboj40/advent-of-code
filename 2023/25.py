# 25   00:36:46    873      0   00:36:47    756      0

from aocd.models import Puzzle
import networkx as nx
import re


def solve(indata):
    G = nx.Graph()

    for row in indata:
        key, vals = row.split(":")
        for val in vals.split():
            G.add_edge(key, val)

    cut = nx.minimum_edge_cut(G)
    G.remove_edges_from(cut)

    a, b = nx.connected_components(G)

    return len(a) * len(b)


if __name__ == "__main__":
    puzzle_input = Puzzle(day=25, year=2023).input_data.split("\n")
    print(f"\nresult: {solve(puzzle_input)}")
