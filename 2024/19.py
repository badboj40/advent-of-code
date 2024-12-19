# 19   00:14:30  1980      0   00:16:30  1287      0

from aocd.models import Puzzle
import time
import functools


@functools.cache
def explore(l, goal):
    res = [0]
    for t in l:
        if t == goal:
            res += [1]
        elif t == goal[:len(t)]:
            res += [explore(l, goal[len(t):])]
    return sum(res)


if __name__ == "__main__":
    t0 = time.time()

    puzzle_input = Puzzle(2024, 19).input_data.split("\n")
    towels = tuple(puzzle_input[0].split(", "))
    patterns = puzzle_input[2:]

    result = [explore(towels, pattern) for pattern in patterns]
    p1 = sum(r > 0 for r in result)
    p2 = sum(result)

    print(f"\npart1: {p1}\npart2: {p2}\n\ntime: {time.time()-t0}")