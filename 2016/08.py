from aocd.models import Puzzle
from aocd import submit
import numpy as np
import re
import time

directory, filename = __file__.split('/')[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')
# indata = puzzle.example_data.split('\n')

WIDTH = 50
HEIGHT = 6

pixels = np.array([[0]*WIDTH for _ in range(HEIGHT)])

def part1():
    for row in indata:
        A, B = map(int, re.findall(r'\d+', row))
        if 'rect' in row:
            for y in range(B):
                for x in range(A):
                    pixels[y][x] = 1
        if 'row' in row:
            pixels[A] = np.roll(pixels[A], B)
        if 'column' in row:
            pixels[:,A] = np.roll(pixels[:,A], B)
    return sum(sum(row) for row in pixels)


def part2():
    print()
    for row in pixels:
        print(''.join('#' if x else '.' for x in row))
    return input("\nWhat code is displayed?\n\n").upper()


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
