#  1   00:04:45  1812      0   00:08:18  2107      0

from aocd.models import Puzzle
import time


def part1(indata):
    indata = [[int(x) for x in row.split('   ')] for row in indata]
    a = sorted([x[0] for x in indata])
    b = sorted([x[1] for x in indata])
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i]-b[i])
    return sum


def part2(indata):
    indata = [[int(x) for x in row.split('   ')] for row in indata]
    a = set([x[0] for x in indata])
    b = sorted([x[1] for x in indata])
    sum = 0
    for x in a:
        sum += x * b.count(x)
    return sum


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n")

    part1_answer = part1(puzzle_input)
    print("\npart1:", part1_answer)

    part2_answer = part2(puzzle_input)
    print("\npart2:", part2_answer)
        
    print("\ntime:", time.time()-t0)