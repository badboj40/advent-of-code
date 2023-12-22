# 22   01:21:05   1913      0   01:46:00   1761      0

# Kinda slow, runs in ~9 seconds with pypy3

from aocd.models import Puzzle
import re

from collections import deque
from copy import deepcopy


def parse(indata):
    bricks = [list(map(int, re.findall(r"\d+", row))) for row in indata]
    return dict(sorted(enumerate(bricks), key=lambda x: x[1][2]))


def collision(brick1, brick2):
    a0, b0, c0, a1, b1, c1 = brick1
    x0, y0, z0, x1, y1, z1 = brick2

    x_overlap = a0 <= x0 <= a1 or x0 <= a0 <= x1
    y_overlap = b0 <= y0 <= b1 or y0 <= b0 <= y1
    z_overlap = c0 <= z0 <= c1 or z0 <= c0 <= z1

    return x_overlap and y_overlap and z_overlap


def fall(bricks):
    supported_by = {i: set() for i in bricks.keys()}
    supporting = {i: set() for i in bricks.keys()}
    for i, brick in bricks.items():
        falling = True
        while falling:
            brick[2] -= 1 
            brick[5] -= 1  

            if brick[2] == 0:
                falling = False
                continue

            for j, other in bricks.items():
                if i != j and collision(brick, other):
                    supported_by[i].add(j)
                    supporting[j].add(i)
                    falling = False

        brick[2] += 1 # Undo last invalid step
        brick[5] += 1

    return supported_by, supporting


def bfs(start, supported_by, supporting):
    supported_by = deepcopy(supported_by)
    supporting = deepcopy(supporting)
    res = 0
    Q = deque([start])
    while Q:
        brick = Q.popleft()
        for other in supporting[brick]:
            supported_by[other] -= {brick}
            if not supported_by[other]:
                Q.append(other)
                res += 1
    return res


def solve(indata):
    bricks = parse(indata)
    supported_by, supporting = fall(bricks)
    a = sum(all(supported_by[j] - {i} for j in supporting[i]) for i in bricks)
    b = sum(bfs(i, supported_by, supporting) for i in bricks)
    return a, b


if __name__ == "__main__":
    puzzle = Puzzle(day=22, year=2023)
    puzzle_input = puzzle.input_data.split("\n")
    part1_answer, part2_answer = solve(puzzle_input)
    print(f"\npart1: {part1_answer}\npart2: {part2_answer}")
