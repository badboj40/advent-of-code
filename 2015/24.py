from aocd.models import Puzzle
from aocd import submit
import itertools
import numpy as np
import time

directory, filename = __file__.split('/')[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
weights = [int(x) for x in puzzle.input_data.split('\n')]

"""
Since the packages are sorted (smallest to largest) I assumed
that the group with the smallest number of packages would be the optimal
solution. It worked, but I'm not sure if it's just a lucky coincidence.
"""


def solve(n):
    for i in range(len(weights)):
        for c in itertools.combinations(weights, i):
            if sum(c) == sum(weights) // n:
                return np.prod(c)


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = solve(3)
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = solve(4)
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
