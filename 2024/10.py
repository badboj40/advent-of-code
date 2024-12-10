# 10   00:12:41  1558      0   00:25:15  3018      0

from aocd.models import Puzzle
import time


def explore(G, y, x):
    if G[y][x] == 9:
        return [(y, x)]
    res = []
    for ny, nx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
        if 0 <= ny < len(G) and 0 <= nx < len(G[0]) and G[ny][nx] == G[y][x] + 1:
            res += explore(G, ny, nx)
    return res


def solve(G):
    trailheads = [(y, x) for y in range(len(G)) for x in range(len(G[0])) if G[y][x] == 0]
    p1 = p2 = 0
    for y, x in trailheads:
        trail_ends = explore(G, y, x)
        p1 += len(set(trail_ends))
        p2 += len(trail_ends)
    return p1, p2


if __name__ == "__main__":
    t0 = time.time()
    G = [[*map(int, row)] for row in Puzzle(2024, 10).input_data.split("\n")]
    p1, p2 = solve(G)
    print("\npart1:", p1)
    print("\npart2:", p2)
    print("\ntime:", time.time()-t0)