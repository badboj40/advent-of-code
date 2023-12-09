# 9   01:58:07  11766      0   02:04:29  11386      0

from aocd.models import Puzzle
from aocd import submit
import time


def diff(x):
    return [x[i + 1] - x[i] for i in range(len(x) - 1)]


def part1(indata):
    res = 0
    for row in indata:
        prev = [int(x) for x in row.split()]
        diffs = [prev[-1]]
        while set(prev := diff(prev)) != {0}:
            diffs.append(prev[-1])

        res += sum(diffs)

    return res


def part2(indata):
    res = 0
    for row in indata:
        prev = [int(x) for x in row.split()]
        diffs = [prev[0]]
        while set(prev := diff(prev)) != {0}:
            diffs.append(prev[0])

        interpolation = 0
        for d in diffs[::-1]:
            interpolation = d - interpolation
        res += interpolation

    return res


if __name__ == "__main__":
    puzzle = Puzzle(day=9, year=2023)
    puzzle_input = puzzle.input_data.split("\n")

    part1_answer = part1(puzzle_input)
    part2_answer = part2(puzzle_input)
    print(f"\npart1: {part1_answer}\npart2: {part2_answer}")
