from aocd.models import Puzzle
from aocd import submit
import numpy as np
import re
import time

directory, filename = __file__.split('/')[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')


def solve(a, b):
    i = 0
    while 0 <= i < len(indata):
        instruction = [x.strip(',') for x in indata[i].split()]
        match instruction[0]:
            case 'hlf':
                a, b = (a//2, b) if instruction[1] == 'a' else (a, b//2)
                i += 1
            case 'tpl':
                a, b = (a*3, b) if instruction[1] == 'a' else (a, b*3)
                i += 1
            case 'inc':
                a, b = (a+1, b) if instruction[1] == 'a' else (a, b+1)
                i += 1
            case 'jmp':
                i += int(instruction[1])
            case 'jie':
                i += int(instruction[2]) if eval(instruction[1]) % 2 == 0 else 1
            case 'jio':
                i += int(instruction[2]) if eval(instruction[1]) == 1 else 1
    return b


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = solve(0, 0)
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = solve(1, 0)
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
