# 10       >24h  46575      0       >24h  37203      0

from aocd.models import Puzzle

import numpy as np
from matplotlib.path import Path


UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)

directions = {
    "|": {UP, DOWN},
    "-": {LEFT, RIGHT},
    "L": {UP, RIGHT},
    "J": {UP, LEFT},
    "7": {LEFT, DOWN},
    "F": {RIGHT, DOWN},
}


def move(pos, dy, dx):
    return pos[0] + dy, pos[1] + dx


def get_start(grid):
    start = tuple(np.argwhere(grid == "S")[0])
    for dy, dx in (UP, DOWN, LEFT, RIGHT):
        dirs = directions[grid[move(start, dy, dx)]]
        if (-dy, -dx) in dirs:
            return start, dy, dx


def get_loop(grid):
    start, dy, dx = get_start(grid)
    loop = [start]
    cur = move(start, dy, dx)
    while cur != start:
        loop.append(cur)
        dy, dx = (directions[grid[cur]] - {(-dy, -dx)}).pop()
        cur = move(cur, dy, dx)
    return loop


def solve(grid):
    loop = get_loop(grid)
    path = Path(loop)

    inside = 0
    for point in np.ndindex(grid.shape):
        if point not in loop and path.contains_point(point):
            inside += 1

    return len(loop) // 2, inside


if __name__ == "__main__":
    puzzle = Puzzle(day=10, year=2023)
    grid = np.array([*map(list, puzzle.input_data.split("\n"))])

    part1_answer, part2_answer = solve(grid)
    print(f"\npart1: {part1_answer}\npart2: {part2_answer}")
