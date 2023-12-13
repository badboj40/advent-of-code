# 13   00:19:48   1061      0   01:22:34   3801      0

from aocd.models import Puzzle
from aocd import submit
import time


def mirror_at_index(terrain, i):
    for j in range(min(i, len(terrain) - i)):
        if terrain[i - 1 - j] != terrain[i + j]:
            return False
    return True


def mirror(terrain, old_solution=0):
    for i in range(1, len(terrain)):
        if i != old_solution and mirror_at_index(terrain, i):
            return i
    return 0


def smudge(terrain):
    old_i = mirror(terrain)

    for y in range(len(terrain)):
        for x in range(len(terrain[y])):
            terrain[y][x] = "#" if terrain[y][x] == "." else "."

            i = mirror(terrain, old_i)
            if i != old_i and i != 0:
                return i

            terrain[y][x] = "#" if terrain[y][x] == "." else "."

    return 0


def part1(indata):
    terrains = [[list(row) for row in terrain.split("\n")] for terrain in indata]
    transposed = [[list(r) for r in zip(*t)] for t in terrains]
    return sum([100 * mirror(t1) + mirror(t2) for t1, t2 in zip(terrains, transposed)])


def part2(indata):
    terrains = [[list(row) for row in terrain.split("\n")] for terrain in indata]
    transposed = [[list(r) for r in zip(*t)] for t in terrains]
    return sum([100 * smudge(t1) + smudge(t2) for t1, t2 in zip(terrains, transposed)])


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split("/")[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n\n")

    part1_answer = part1(puzzle_input)
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2(puzzle_input)
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
