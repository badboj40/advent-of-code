# 20   00:32:00  1542      0   02:38:48  3779      0

from aocd.models import Puzzle
import time
from collections import deque


orto = [(-1,0), (0,1), (1,0), (0,-1)] # N, E, S, W


def get_costs(G, start):
    costs = {}
    Q = deque([(0, *start)])

    while Q:
        cost, y, x = Q.popleft()
        if (y, x) in costs or G[y][x] == "#":
            continue
        costs[(y, x)] = cost

        if G[y][x] == "E":
            return sorted((cost, y, x) for (y, x), cost in costs.items())

        Q.extend((cost + 1, ny, nx) for ny, nx in [(y+dy, x+dx) for dy, dx in orto])

    return {}


def solve(G, n):
    start = [(y, x) for y in range(len(G)) for x in range(len(G[0])) if G[y][x] == "S"][0]
    costs = get_costs(G, start)

    res = 0
    for i, (cost1, y1, x1) in enumerate(costs):
        for (cost2, y2, x2) in costs[i:]:
            dist = abs(y2 - y1) + abs(x2 - x1)
            saved = cost2 - cost1 - dist
            if dist <= n and saved >= 100:
                res += 1

    return res


if __name__ == "__main__":
    t0 = time.time()
    puzzle_input = Puzzle(2024, 20).input_data.split("\n")
    print("part1:", p1:=solve(puzzle_input, 2))
    print("part2:", p2:=solve(puzzle_input, 20))
    print("\ntime:", time.time()-t0)