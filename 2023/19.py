# 19   00:32:58   1969      0   01:03:09   1038      0

from aocd.models import Puzzle
import numpy as np
import re
import time


def parse(indata):
    workflows = {}
    ratings = []
    workflow_done = False
    for row in indata:
        if not workflow_done:
            if row == "":
                workflow_done = True
                continue
            name, workflow = row.split("{")
            workflows[name] = workflow[:-1].split(",")
        else:
            rating = {}
            for key, val in [x.split("=") for x in row[1:-1].split(",")]:
                rating[key] = (int(val), int(val))
            ratings.append(rating)
    return workflows, ratings


def get_overlap(check, rating):
    overlap = {}
    non_overlap = {}
    category, value = re.split("<|>", check)
    a, b = rating[category]
    if "<" in check:
        if b < int(value):
            overlap = rating
        elif int(value) <= a:
            non_overlap = rating
        else:
            overlap = rating.copy()
            non_overlap = rating.copy()
            overlap[category] = (a, int(value) - 1)
            non_overlap[category] = (int(value), b)
    elif ">" in check:
        if a > int(value):
            overlap = rating
        elif int(value) >= b:
            non_overlap = rating
        else:
            overlap = rating.copy()
            non_overlap = rating.copy()
            overlap[category] = (int(value) + 1, b)
            non_overlap[category] = (a, int(value))

    return overlap, non_overlap


def traverse(workflows, rating, key="in"):
    if key not in workflows:
        return [rating] if key == "A" and rating else []

    res = []
    workflow = workflows[key]
    for step in workflow[:-1]:
        if not rating:
            break
        check, new_key = step.split(":")
        overlap, non_overlap = get_overlap(check, rating)
        res += traverse(workflows, overlap, new_key)
        rating = non_overlap

    if rating:
        res += traverse(workflows, rating, workflow[-1])

    return res


def part1(indata):
    workflows, ratings = parse(indata)
    valid = []
    for rating in ratings:
        valid += traverse(workflows, rating)
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
    puzzle_input = puzzle.input_data.split("\n")
    print(f"\npart1: {part1(puzzle_input)}\npart2: {part2(puzzle_input)}")