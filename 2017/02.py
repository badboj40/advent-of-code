from aocd.models import Puzzle
from aocd import submit
import time

directory, filename = __file__.split('/')[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = [[*map(int, row.split())] for row in puzzle.input_data.split('\n')]


def part1():
    return sum([max(row) - min(row) for row in indata])


def part2():
    return sum([x // y for row in indata for x in row for y in row
                if x != y and x % y == 0])


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
