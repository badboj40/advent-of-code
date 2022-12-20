# Solution took 00:16:15

import hashlib
from aocd.models import Puzzle
YEAR, DAY = 2015, 4
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.strip()

def part1():
    i = 0
    while True:
        i += 1
        string = indata + str(i)
        if hashlib.md5(string.encode('UTF-8')).hexdigest()[:5] == '00000':
            return i


def part2():
    i = 0
    while True:
        i += 1
        string = indata + str(i)
        if hashlib.md5(string.encode('UTF-8')).hexdigest()[:6] == '000000':
            return i


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
