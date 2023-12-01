from aocd.models import Puzzle
from aocd import submit
import numpy as np
import re
import time

directory, filename = __file__.split("/")[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split("\n")

indata = [int(x) for x in puzzle.input_data.split("\n")]


def part1():
    return sum(indata)


def part2():
    i, freq, seen = 0, 0, {0}
    while True:
        freq += indata[i % len(indata)]
        if freq in seen:
            return freq
        i += 1
        seen.add(freq)


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    if part2_answer is not None:
        print("\npart2:", part2_answer)
        submit(part2_answer, part="b", day=DAY, year=YEAR)
    else:
        print("\npart2: None")

    print("\ntime:", time.time() - t0)
