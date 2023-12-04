#  4   00:05:48   1030      0   00:15:33   1300      0

from aocd.models import Puzzle
from aocd import submit
import time

directory, filename = __file__.split("/")[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split("\n")


def part1():
    res = 0
    for row in indata:
        win, have = row.split(":")[1].split("|")
        matching = len(set(win.split()) & set(have.split()))
        res += 2 ** (matching - 1) if matching else 0
    return res


def part2():
    cards = {i: 1 for i in range(len(indata))}
    for i, row in enumerate(indata):
        win, have = row.split(":")[1].split("|")
        matching = len(set(win.split()) & set(have.split()))
        for j in range(matching):
            cards[i + j + 1] += cards[i]
    return sum(cards.values())


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
