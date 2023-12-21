# 21   00:08:58    627      0   05:57:29   2745      0

from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time


def parse(indata):
    grid = []
    for y, row in enumerate(indata):
        grid.append(list(row))
        if "S" in row:
            start = (y, row.index("S"))
    return grid, start


def part1(indata):
    grid, start = parse(indata)
    W = H = len(grid)
    step = {start}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for _ in range(64):
        neighbors = [(y + dy, x + dx) for y, x in step for dy, dx in directions]
        step = {
            (ny, nx)
            for ny, nx in neighbors
            if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != "#"
        }
    return len(step)


def part2(indata):
    grid, start = parse(indata)
    edge = (start[0], 0)
    W = H = len(grid)
    step = {start}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    i = 0
    points = []
    while len(points) < 3:
        if edge in step:
            points.append((i, len(step)))
            edge = (edge[0], edge[1] - len(grid))
        neighbors = [(y + dy, x + dx) for y, x in step for dy, dx in directions]
        step = {(ny, nx) for ny, nx in neighbors if grid[ny % H][nx % W] != "#"}
        i += 1

    x, y = zip(*points)
    quadratic = np.poly1d(np.polyfit(x, y, 2))

    return int(quadratic(26501365))


if __name__ == "__main__":
    puzzle = Puzzle(day=21, year=2023)
    puzzle_input = puzzle.input_data.split("\n")
    print(f"\npart1: {part1(puzzle_input)}\npart2: {part2(puzzle_input)}")
