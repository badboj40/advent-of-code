# 12   00:38:34   2634      0   00:52:39    914      0

from aocd.models import Puzzle
from functools import cache


@cache
def traverse(field, count):
    if not field:
        return not count
    if "?" not in field[0]:
        if not count or len(field[0]) != count[0]:
            return 0
        return traverse(field[1:], count[1:])
    a = tuple([x for x in field[0].split("?", 1) if x] + list(field[1:]))
    b = tuple([field[0].replace("?", "#", 1)] + list(field[1:]))
    return traverse(a, count) + traverse(b, count)


def solve(indata, part):
    res = 0
    for row in indata:
        a, b = row.split(" ")
        if part == "b":
            a = "?".join([a] * 5)
            b = ",".join([b] * 5)
        field = tuple(x for x in a.split(".") if x)
        count = tuple(int(x) for x in b.split(","))
        res += traverse(field, count)
    return res


if __name__ == "__main__":
    puzzle = Puzzle(day=12, year=2023)
    puzzle_input = puzzle.input_data.split("\n")

    part1_answer = solve(puzzle_input, "a")
    part2_answer = solve(puzzle_input, "b")
    print(f"\npart1: {part1_answer}\npart2: {part2_answer}")
