# 18   01:18:29  5920      0   01:26:10  5447      0

from aocd.models import Puzzle
from collections import deque
import time


SIZE = 71
orto = [(-1,0), (0,1), (1,0), (0,-1)] # N, E, S, W


def explore(G):
    Q = deque([(0, 0, 0)])
    visited = G.copy()

    while Q:
        steps, x, y= Q.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == y == SIZE - 1:
            return steps

        for nx, ny in [(x+dx, y+dy) for dx, dy in orto if 0 <= x+dx < SIZE and 0 <= y+dy < SIZE]:
            Q.append((steps + 1, nx, ny))

    return float("inf")        


def solve(indata):
    stones = [tuple(map(int,row.split(","))) for row in indata]
    G = set(stones[:1024])
    p1 = explore(G)

    for (x, y) in stones[1024:]:
        G.add((x, y))
        if explore(G) == float("inf"):
            p2 = f"{x},{y}"
            break
    return p1, p2


if __name__ == "__main__":
    t0 = time.time()
    puzzle_input = Puzzle(2024, 18).input_data.split("\n")
    p1, p2 = solve(puzzle_input)
    print(f"\npart1: {p1}\npart2: {p2}\n\ntime: {time.time()-t0}")