# 22   00:14:55  2235      0   00:43:34  1484      0

from aocd.models import Puzzle
from collections import defaultdict
import time


def evolve(n):
    n = n ^ (n * 64) % 16777216
    n = n ^ (n // 32) % 16777216
    n = n ^ (n * 2048) % 16777216
    return n


def get_data(n):
    x = n % 10
    pattern = ()
    patterns = {}

    for _ in range(2000):
        n = evolve(n)
        pattern = *pattern[-3:], n%10 - x
        x = n % 10
        if pattern not in patterns and len(pattern) == 4:
            patterns[pattern] = x

    return n, patterns


def solve(indata):
    numbers, patterns = zip(*[get_data(n) for n in indata])

    pattern_sum = defaultdict(int)
    for pattern in patterns:
        for key, value in pattern.items():
            pattern_sum[key] += value

    return sum(numbers), max(pattern_sum.values())


if __name__ == "__main__":
    t0 = time.time()
    puzzle_input = [*map(int, Puzzle(2024, 22).input_data.split("\n"))]
    p1, p2 = solve(puzzle_input)
    print("\npart1:", p1)
    print("\npart2:", p2)
    print("\ntime:", time.time()-t0)