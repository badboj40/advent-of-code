# 16   00:29:14   1514      0   00:37:05   1425      0

from aocd.models import Puzzle
import time


def next_beam(grid, y, x, dirr):
    y += 1 if dirr == "v" else -1 if dirr == "^" else 0
    x += 1 if dirr == ">" else -1 if dirr == "<" else 0
    mirrors = {
        "/": {">": "^", "^": ">", "<": "v", "v": "<"},
        "\\": {">": "v", "v": ">", "<": "^", "^": "<"},
        "|": {"^": "^", "v": "v", "<": "v^", ">": "v^"},
        "-": {"<": "<", ">": ">", "^": "<>", "v": "<>"},
        ".": {"<": "<", ">": ">", "^": "^", "v": "v"},
    }
    mirror = grid[y][x] if 0 <= y < len(grid) and 0 <= x < len(grid[0]) else None
    dirr = mirrors[mirror][dirr] if mirror else ""
    return [(y, x, d) for d in dirr]


def solve(grid, start):
    beams = [start]
    cache = set()
    energized = set()
    while beams:
        y, x, dirr = beams.pop()
        energized.add((y, x))

        if (y, x, dirr) not in cache:
            cache.add((y, x, dirr))
            beams += next_beam(grid, y, x, dirr)

    return len(energized) - 1


def part1(indata):
    start = (0, -1, ">")
    return solve(indata, start)


def part2(indata):
    starts = []

    for y in range(len(indata)):
        starts.append((y, -1, ">"))
        starts.append((y, len(indata[0]), "<"))

    for x in range(len(indata[0])):
        starts.append((-1, x, "v"))
        starts.append((len(indata), x, "^"))

    return max(solve(indata, start) for start in starts)


if __name__ == "__main__":
    puzzle = Puzzle(day=16, year=2023)
    puzzle_input = puzzle.input_data.split("\n")
    print(f"\npart1: {part1(puzzle_input)}\npart2: {part2(puzzle_input)}")
