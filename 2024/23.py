# 23   00:13:57  1533      0   00:17:29   609      0

from aocd.models import Puzzle
import networkx as nx
import time


def solve(indata):
    edges = [row.split("-") for row in indata]
    G = nx.Graph()
    G.add_edges_from(edges)

    cliques = [*nx.enumerate_all_cliques(G)]

    size_three = {tuple(sorted(c)) for c in cliques if len(c) == 3 and any(x[0] == "t" for x in c)}
    p1 = len(size_three)

    biggest = max(cliques, key=len)
    p2 = ",".join(sorted(biggest))

    return p1, p2


if __name__ == "__main__":
    t0 = time.time()

    puzzle_input = Puzzle(2024, 23).input_data.split("\n")

    p1, p2 = solve(puzzle_input)
    assert p1 == 1110 and p2 == "ej,hm,ks,ms,ns,rb,rq,sc,so,un,vb,vd,wd"
    print(f"part1: {p1}\npart2: {p2}\n\ntime: {time.time()-t0}")