#  6   00:07:46   1602      0   00:12:22   1924      0

from aocd.models import Puzzle
from aocd import submit
import re
import time


def part1(indata):
    times, dist = [[int(x) for x in re.findall(r"\d+", row)] for row in indata]
    res = 1
    for t, d in zip(times, dist):
        res *= sum(i * (t - i) > d for i in range(t))
    return res


def part2(indata):
    t, d = [int("".join(re.findall(r"\d+", row))) for row in indata]
    return sum(i * (t - i) > d for i in range(t))


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split("/")[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n")

    part1_answer = part1(puzzle_input)
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2(puzzle_input)
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
