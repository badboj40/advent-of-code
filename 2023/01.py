#  1   00:09:08  4509      0   00:36:19  4110      0

from aocd.models import Puzzle
from aocd import submit
import re
import time

directory, filename = __file__.split("/")[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split("\n")

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part1():
    count = 0
    for row in indata:
        x = re.findall(r"\d", row)
        count += int(x[0] + x[-1])
    return count


def part2():
    count = 0
    for x in indata:
        x = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", x)

        a = digits[x[0]] if x[0] in digits else x[0]
        b = digits[x[-1]] if x[-1] in digits else x[-1]
        count += int(a + b)
    return count


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
