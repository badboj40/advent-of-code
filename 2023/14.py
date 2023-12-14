#  14   00:06:39    464      0   00:40:50   1268      0

from aocd.models import Puzzle
import numpy as np


def roll(grid):
    for y, row in enumerate(grid):
        if y == 0:
            continue
        for x, tile in enumerate(row):
            if tile == "O":
                yi = y - 1
                while yi >= 0 and grid[yi][x] == ".":
                    grid[yi][x] = "O"
                    grid[yi + 1][x] = "."
                    yi -= 1
    return grid


def cycle(grid):
    for i in range(4):
        grid = roll(grid)
        grid = np.rot90(grid, 3)
    return [list(row) for row in grid]


def get_load(grid):
    return sum(row.count("O") * (len(grid) - y) for y, row in enumerate(grid))


def part1(indata):
    grid = [list(row) for row in indata]
    grid = roll(grid)
    return get_load(grid)


def part2(indata):
    grid = [list(row) for row in indata]

    history = [""]

    total_cycles = 1000000000
    loop_start = None
    loop_size = None

    i = 1
    while True:
        grid = cycle(grid)
        grid_str = "\n".join("".join(row) for row in grid)
        if grid_str in history:
            loop_start = history.index(grid_str)
            loop_size = i - loop_start
            break
        history.append(grid_str)
        i += 1

    goal_cycle = (total_cycles - loop_start) % loop_size + loop_start
    grid = [list(row) for row in history[goal_cycle].split("\n")]

    return get_load(grid)


if __name__ == "__main__":
    puzzle = Puzzle(day=14, year=2023)
    puzzle_input = puzzle.input_data.split("\n")
    print(f"\npart1: {part1(puzzle_input)}\npart2: {part2(puzzle_input)}")
