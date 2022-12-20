# Solution took 00:09:59

from aocd.models import Puzzle
YEAR, DAY = 2015, 2
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')[:-1]

def part1():
    res = 0
    for row in indata:
        l, w, h = sorted([int(x) for x in row.split('x')])
        res += 3 * l * w + 2 * w * h + 2 * h * l
    return res


def part2():
    res = 0
    for row in indata:
        l, w, h = sorted([int(x) for x in row.split('x')])
        res += 2 * l + 2 * w + l * w * h
    return res


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
