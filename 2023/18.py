#  18   01:03:09   3516      0   01:47:47   2271      0

from aocd.models import Puzzle
from aocd import submit
import numpy as np
import re
import time
import sys

sys.setrecursionlimit(100000)


def show_holes(holes):
    minx, maxx = min(x for y, x in holes), max(x for y, x in holes)
    miny, maxy = min(y for y, x in holes), max(y for y, x in holes)

    print(minx, maxx, miny, maxy)
    print()
    for y in range(miny, maxy + 1):
        row = ""
        for x in range(minx, maxx + 1):
            if (y, x) not in holes:
                row += '.'
            else:
                row += '#'
        print(row)


def part1(indata):
    y, x = 0, 0
    holes = [(y, x)]
    for row in indata:
        dirr, length, _ = row.split()
        for _ in range(int(length)):
            y += 1 if dirr == "D" else -1 if dirr == "U" else 0
            x += 1 if dirr == "R" else -1 if dirr == "L" else 0
            holes.append((y, x))

    holes = set(holes)

    def floodfill(y, x):
        if (y, x) not in holes:
            holes.add((y, x))
            floodfill(y + 1, x)
            floodfill(y - 1, x)
            floodfill(y, x + 1)
            floodfill(y, x - 1)
    
    floodfill(1, 1)
    
    return len(holes)


def part2(indata):
    y, x = 0, 0
    holes = []
    area = 0
    line = 0
    for row in indata:
        instr = row.split('#')[1].split(')')[0]
        l = int(instr[:-1], 16)
        dirr = instr[-1]
        new_y = y + l if dirr == "1" else y - l if dirr == "3" else y
        new_x = x + l if dirr == "0" else x - l if dirr == "2" else x
        # Shoelace formula
        area += x * new_y - y * new_x
        line += l
        y, x = new_y, new_x

    return area // 2 + line // 2 + 1
    
    


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n")
    example_input = puzzle.examples[0].input_data.split("\n")

    ex1 = part1(example_input)
    ex1_answer = int(puzzle.examples[0].answer_a)
    assert ex1 == ex1_answer, f"Ex1: expected {ex1_answer}, got {ex1}"

    part1_answer = part1(puzzle_input)
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    ex2 = part2(example_input)
    ex2_answer = 952408144115
    assert ex2 == ex2_answer, f"Ex2: expected {ex2_answer}, got {ex2}"

    part2_answer = part2(puzzle_input)
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)
        
    print("\ntime:", time.time()-t0)