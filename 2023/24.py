#  24   00:52:19   1258      0   01:38:49    513      0

from aocd.models import Puzzle
import numpy as np
import re
from itertools import combinations
from z3 import *


def line_intersection(line1, line2):
    MIN, MAX = 2e14, 4e14

    a, b, _, va, vb, _ = line1
    x, y, _, vx, vy, _ = line2

    denom = va * vy - vb * vx

    t1 = ((x - a) * vy - (y - b) * vx) / denom if denom != 0 else -1
    t2 = ((a - x) * vb - (b - y) * va) / (-denom) if denom != 0 else -1

    # Both times must be positive, otherwise the intersection is invalid
    if t1 < 0 or t2 < 0:
        return False

    x = a + t1 * va
    y = b + t1 * vb
    return MIN <= x <= MAX and MIN <= y <= MAX


def part1(indata):
    vectors = [list(map(int, re.findall(r"-?\d+", row))) for row in indata]
    return sum(line_intersection(a, b) for a, b in combinations(vectors, 2))


def part2(indata):
    vectors = [list(map(int, re.findall(r"-?\d+", row))) for row in indata][:10]
    x, y, z, vx, vy, vz = [Int(var) for var in "x,y,z,vx,vy,vz".split(",")]
    t = [Int(f"t{i}") for i in range(len(vectors))]

    S = Solver()
    for i, (a, b, c, va, vb, vc) in enumerate(vectors):
        S.add(x + vx * t[i] == a + va * t[i])
        S.add(y + vy * t[i] == b + vb * t[i])
        S.add(z + vz * t[i] == c + vc * t[i])

    if S.check() == sat:
        model = S.model()
        return str(model.eval(x + y + z))


if __name__ == "__main__":
    puzzle_input = Puzzle(day=24, year=2023).input_data.split("\n")
    print(f"\npart1: {part1(puzzle_input)}\npart2: {part2(puzzle_input)}")
