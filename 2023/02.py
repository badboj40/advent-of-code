#  2   00:18:06  3841      0   00:23:56  3805      0

from aocd.models import Puzzle
from aocd import submit
import time

directory, filename = __file__.split("/")[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split("\n")


def cube_count(subset):
    r, g, b = (0, 0, 0)
    for cube in subset.split(","):
        x, color = cube.split()
        r = int(x) if color == "red" else r
        g = int(x) if color == "green" else g
        b = int(x) if color == "blue" else b
    return (r, g, b)


def is_valid(subset):
    r, g, b = cube_count(subset)
    return r <= 12 and g <= 13 and b <= 14


def part1():
    res = 0
    for i, game in enumerate(indata):
        subsets = game.split(":")[1].split(";")
        if all(is_valid(subset) for subset in subsets):
            res += i + 1
    return res


def part2():
    power = 0
    for i, game in enumerate(indata):
        subsets = game.split(":")[1].split(";")
        cubes = [cube_count(subset) for subset in subsets]
        r, g, b = zip(*cubes)  # split columns into separate lists
        power += max(r) * max(g) * max(b)
    return power


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    if part1_answer is not None:
        submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    if part2_answer is not None:
        submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
