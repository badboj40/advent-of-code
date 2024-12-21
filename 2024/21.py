# 21   01:59:12  1595      0   04:27:52  1909      0

from aocd.models import Puzzle
from functools import cache
import time


NUMERIC = "789456123 0A"
DIRECTIONAL = " ^A<v>"


@cache
def bfs(keypad, start, goal):
    start_pos = divmod(keypad.find(start),3)
    goal_pos = divmod(keypad.find(goal), 3)
    dist = abs(goal_pos[0] - start_pos[0]) + abs(goal_pos[1] - start_pos[1])
    Q = [(*start_pos, "")]

    results = []
    while Q:
        y, x, path = Q.pop(0)

        if not 0 <= 3*y+x < len(keypad) or keypad[3*y+x] == " " or len(path) > dist:
            continue

        if (y, x) == goal_pos:
            results += [path + "A"]
            continue

        for (dir, dy, dx) in [("^", -1, 0), (">", 0, 1), ("v", 1, 0), ("<", 0, -1)]:
            Q.append((y + dy, x + dx, path + dir))

    return results


@cache
def explore(moves, n, keypad=DIRECTIONAL):
    if n == 0:
        return len(moves)
    res = 0
    for prev, cur in zip("A" + moves, moves):
        paths = bfs(keypad, prev, cur)
        res += min(explore(p, n-1) for p in paths)
    return res


def solve(indata, n):
    res = 0
    for code in indata:
        shortest = explore(code, n+1, NUMERIC)
        res += shortest * int(code[:-1])
    return res


if __name__ == "__main__":
    t0 = time.time()
    puzzle_input = Puzzle(2024, 21).input_data.split("\n")
    print("part1:", solve(puzzle_input, 2))
    print("part2:", solve(puzzle_input, 25))
    print("\ntime:", time.time()-t0)