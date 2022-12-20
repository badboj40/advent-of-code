# Solution took 00:04:52

from aocd.models import Puzzle
YEAR, DAY = 2015, 1
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data

def part1():
    res = 0
    for c in indata:
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
    return res


def part2():
    res = 0
    for i, c in enumerate(indata):
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
        if res < 0:
            return i+1


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
