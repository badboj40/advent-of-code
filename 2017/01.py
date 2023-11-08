from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time

directory, filename = __file__.split('/')[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data


def part1():
    result = 0
    for i, d in enumerate(indata):
        if d == indata[i-1]:
            result += int(d)
    return result


def part2():
    result = 0
    for i, d in enumerate(indata):
        if d == indata[i-len(indata)//2]:
            result += int(d)
    return result


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
