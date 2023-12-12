# 11   03:36:49  14424      0   12:26:13  27681      0

from aocd.models import Puzzle
import itertools


def parse(indata):
    coords = []
    for y, row in enumerate(indata):
        for x, tile in enumerate(row):
            if tile == "#":
                coords.append((x, y))

    rows = [i for i, row in enumerate(indata) if "#" not in row]
    cols = [i for i, col in enumerate(zip(*indata)) if "#" not in col]

    return coords, rows, cols


def solve(indata, N):
    coords, rows, cols = parse(indata)

    res = 0
    for a, b in itertools.combinations(coords, 2):
        x0, x1 = min(a[0], b[0]), max(a[0], b[0])
        y0, y1 = min(a[1], b[1]), max(a[1], b[1])

        res += (x1 - x0) + (y1 - y0)  # Manhattan distance
        res += sum([N - 1 for row in rows if y0 < row < y1])  # y expansions
        res += sum([N - 1 for col in cols if x0 < col < x1])  # x expansions

    return res


if __name__ == "__main__":
    puzzle = Puzzle(day=11, year=2023)
    puzzle_input = puzzle.input_data.split("\n")

    part1_answer = solve(puzzle_input, 2)
    part2_answer = solve(puzzle_input, 1_000_000)
    print(f"\npart1: {part1_answer}\npart2: {part2_answer}")
