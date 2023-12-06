#  6   00:07:46   1602      0   00:12:22   1924      0

from aocd.models import Puzzle
from aocd import submit
import re
import time


def part1(indata):
    times = [int(x) for x in re.findall(r"\d+", indata[0])]
    dist = [int(x) for x in re.findall(r"\d+", indata[1])]
    res = 1
    for t, d in zip(times, dist):
        summ = 0
        for i in range(t + 1):
            if i * (t - i) > d:
                summ += 1
        res *= summ
    return res


def part2(indata):
    times = int("".join(re.findall(r"\d+", indata[0])))
    dist = int("".join(re.findall(r"\d+", indata[1])))
    summ = 0
    for i in range(times + 1):
        if i * (times - i) > dist:
            summ += 1
    return summ


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
