from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time

directory, filename = __file__.split('/')[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = int(puzzle.input_data)

"""
Brute force solution :(
"""


def get_factors(n):
    factors = set()
    for i in range(1, int(np.sqrt(n))+1):
        if n % i == 0:
            factors |= {i, n//i}
    return factors


def part1():
    n = 1
    while sum(get_factors(n)) * 10 < indata:
        n += 1
    return n


def part2():
    n = 1
    while sum(f for f in get_factors(n) if n/f <= 50) * 11 < indata:
        n += 1
    return n


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
