# 14   00:18:41  1823      0   00:39:15  1307      0

from aocd.models import Puzzle
import re
import time

H, W = 103, 101


def show(robots):
    G = {(y, x) for x, y, *_ in robots}
    for y in range(H):
        print("".join(["#" if (y, x) in G else "." for x in range(W)]))


def largest_cluster(robots):
    G = {(y, x) for x, y, *_ in robots}
    visited = set()

    def dfs(y, x):
        if (y, x) not in G or (y, x) in visited:
            return 0
        visited.add((y, x))
        return 1 + sum(dfs(y+dy, x+dx) for dy,dx in [(-1,0), (0,1), (1,0), (0,-1)])
    
    return max(dfs(y, x) for y,x in G)


def score(robots):
    q1 = len([r for r in robots if r[0] < W//2 and r[1] < H//2])
    q2 = len([r for r in robots if r[0] > W//2 and r[1] < H//2])
    q3 = len([r for r in robots if r[0] < W//2 and r[1] > H//2])
    q4 = len([r for r in robots if r[0] > W//2 and r[1] > H//2])
    return q1 * q2 * q3 * q4


def solve(indata):
    robots = [map(int, re.findall(r'\d+|-\d+', row)) for row in indata]
    p1 = p2 = i = 0
    while not p2:
        i += 1
        robots = [((x+dx) % W, (y+dy) % H, dx, dy) for x, y, dx, dy in robots]
        if i == 100:
            p1 = score(robots)
        if largest_cluster(robots) > 100:
            # show(robots)
            p2 = i
    return p1, p2


if __name__ == "__main__":
    t0 = time.time()
    puzzle_input = Puzzle(2024, 14).input_data.split("\n")
    p1, p2 = solve(puzzle_input)
    print("\npart1:", p1)
    print("\npart2:", p2)
    print("\ntime:", time.time()-t0)