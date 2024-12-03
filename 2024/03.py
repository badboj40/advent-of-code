#  3   00:09:14  3754      0   00:30:25  6093      0

from aocd.models import Puzzle
import re
import time


def part1(indata):
    operations = re.findall(r"mul\(\d+,\d+\)", indata)
    s = 0
    for op in operations:
        a, b = map(int, re.findall(r'\d+', op))
        s += a * b
    return s


def part2(indata):
    operations = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", indata)
    s = 0
    active = True
    for op in operations:
        if 'mul' in op and active:
            a,b = map(int, re.findall(r'\d+',op))
            s += a * b
        elif op == "don't()":
            active = False
        elif op == "do()":
            active = True
    return s


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data

    part1_answer = part1(puzzle_input)
    print("\npart1:", part1_answer)

    part2_answer = part2(puzzle_input)
    print("\npart2:", part2_answer)
        
    print("\ntime:", time.time()-t0)