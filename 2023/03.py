#  3   05:54:40  28058      0   05:57:54  21817      0

from aocd.models import Puzzle
from aocd import submit
import time

directory, filename = __file__.split("/")[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split("\n")


def is_adjacent(number, symbol):
    y0, x0, length, num = number
    sy, sx = symbol
    coords = [(y0, x0 + dx) for dx in range(length)]

    for y, x in coords:
        if abs(sy-y) <= 1 and abs(sx-x) <= 1:
            return True
    return False


def parse_indata():
    symbols = []  # y, x
    numbers = []  # y, x, length, num
    for y in range(len(indata)):
        num = ""
        for x in range(len(indata[y])):
            if indata[y][x] == '.':
                if num != "":
                    numbers.append((y, x - len(num), len(num), int(num)))
                    num = ""
            elif indata[y][x].isdigit():
                    num += indata[y][x]
            else:
                if num != "":
                    numbers.append((y, x - len(num), len(num), int(num)))
                    num = ""
                symbols.append((y, x))
        if num != "":
            numbers.append((y, x - len(num), len(num), int(num)))

    return numbers, symbols


def part1():
    numbers, symbols = parse_indata()
    res = 0

    for n in numbers:
        if any(is_adjacent(n, s) for s in symbols):
            res += n[3]

    return res


def part2():
    numbers, symbols = parse_indata()
    res = 0

    for s in symbols:
        adj = [n for n in numbers if is_adjacent(n, s)]
        if len(adj) == 2:
            res += adj[0][3] * adj[1][3]

    return res


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
