#  2   00:14:15  4717      0   00:19:45  2751      0

from aocd.models import Puzzle
import re
import time


def is_safe(row):
    if row not in [sorted(row), sorted(row, reverse=True)]:
        return False
    for i in range(len(row)-1):
        if not 1 <= abs(row[i] - row[i+1]) <= 3:
            return False
    return True


def part1(indata):
    return sum(is_safe(row) for row in indata)


def part2(indata):
    s = 0
    for row in indata:
        for i in range(len(row)):
            if is_safe(row[:i] + row[i+1:]): 
                s += 1
                break
    return s


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = [[*map(int, re.findall(r'\d+', row))] for row in puzzle.input_data.split('\n')]

    part1_answer = part1(puzzle_input)
    print("\npart1:", part1_answer)

    part2_answer = part2(puzzle_input)
    print("\npart2:", part2_answer)
        
    print("\ntime:", time.time()-t0)