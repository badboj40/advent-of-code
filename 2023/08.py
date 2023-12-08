# 8   00:11:22   2842      0   02:10:22   9277      0

from aocd.models import Puzzle
import re
import math


def parse(indata):
    turns = indata[0]
    path = {}
    for row in indata[2:]:
        x, left, right = re.findall(r"[A-Z]+", row)
        path[x] = (left, right)
    return turns, path


def traverse(start, turns, path, part):
    i = 0
    cur = start
    while part == "a" and cur != "ZZZ" or part == "b" and cur[-1] != "Z":
        cur = path[cur][0] if turns[i % len(turns)] == "L" else path[cur][1]
        i += 1
    return i


def solve(turns, path, part):
    if part == "a":
        return traverse("AAA", turns, path, part="a")

    starts = [x for x in path if x[-1] == "A"]
    goals = [traverse(start, turns, path, part="b") for start in starts]
    return math.lcm(*goals)


if __name__ == "__main__":
    puzzle = Puzzle(day=8, year=2023)
    puzzle_input = puzzle.input_data.split("\n")
    turns, path = parse(puzzle_input)

    part1_answer = solve(turns, path, "a")
    part2_answer = solve(turns, path, "b")
    print(f"\npart1: {part1_answer}\npart2: {part2_answer}")