# 19   00:32:58   1969      0   01:03:09   1038      0

from aocd.models import Puzzle
import numpy as np
import re


def parse(indata):
    wd, rd = indata.split("\n\n")
    wfs = {n: w.split(",") for n, w in [x[:-1].split("{") for x in wd.split("\n")]}
    ratings = []
    for row in rd.split("\n"):
        x, m, a, s = map(int, re.findall(r"\d+", row))
        ratings.append({"x": (x, x), "m": (m, m), "a": (a, a), "s": (s, s)})
    return wfs, ratings


def get_overlap(check, rating):
    if not rating:
        return {}, {}
    category, op, val = re.findall("\w+|.", check)
    val = int(val)
    a, b = rating[category]
    if op == "<" and b < val or op == ">" and a > val:
        return rating, {}
    elif op == "<" and val <= a or op == ">" and val >= b:
        return {}, rating
    else:
        overlap = (a, val - 1) if op == "<" else (val + 1, b)
        non_overlap = (val, b) if op == "<" else (a, val)
        return {**rating, category: overlap}, {**rating, category: non_overlap}


def traverse(workflows, rating, key="in"):
    if key not in workflows:
        return [rating] if key == "A" and rating else []
    res = []
    for step in workflows[key][:-1]:
        check, new_key = step.split(":")
        overlap, rating = get_overlap(check, rating)
        res += traverse(workflows, overlap, new_key)
    return res + traverse(workflows, rating, workflows[key][-1])


def part1(indata):
    workflows, ratings = parse(indata)
    valid = sum((traverse(workflows, rating) for rating in ratings), [])
    return sum(sum(x[0] for x in r.values()) for r in valid)


def part2(indata):
    workflows, _ = parse(indata)
    rating = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    res = 0
    for r in traverse(workflows, rating):
        res += np.prod([r[1] - r[0] + 1 for r in r.values()])
    return res


if __name__ == "__main__":
    puzzle = Puzzle(day=19, year=2023)
    puzzle_input = puzzle.input_data
    print(f"\npart1: {part1(puzzle_input)}\npart2: {part2(puzzle_input)}")
