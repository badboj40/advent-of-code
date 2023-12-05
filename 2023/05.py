#  5   00:33:24   3612      0   01:46:25   3724      0

from aocd.models import Puzzle
from aocd import submit
import re
import time


def parse_input(indata, part="a"):
    seeds = [int(x) for x in re.findall(r"\d+", indata[0])]
    if part == "b":
        seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    maps = []
    for section in indata[1:]:
        maps.append([[*map(int, row.split())] for row in section.split("\n")[1:]])

    return seeds, maps


def overlaps(a0, a1, b0, b1):
    overlap = (max(a0, b0), min(a1, b1)) if a0 <= b0 < a1 or b0 <= a0 < b1 else None
    non_overlap = (a0, a1) if a1 <= b0 or b1 <= a0 else (b1, a1) if b1 < a1 else None

    return overlap, non_overlap


def get_next_range(seed, conversion_map):
    if not conversion_map:
        return [seed]

    dest, source, length = conversion_map[0]

    overlap, non_overlap = overlaps(seed[0], seed[1], source, source + length)

    result = []
    if overlap:
        result += [(overlap[0] - source + dest, overlap[1] - source + dest)]
    if non_overlap:
        result += get_next_range(non_overlap, conversion_map[1:])

    return result


def traverse(seed, maps, part):
    if not maps:
        return seed if part == "a" else seed[0]

    if part == "a":
        for dest, source, length in maps[0]:
            if source <= seed < source + length:
                return traverse(seed - source + dest, maps[1:], part)
        return traverse(seed, maps[1:], part)

    return min(traverse(s, maps[1:], part) for s in get_next_range(seed, maps[0]))


def solve(indata, part):
    seeds, maps = parse_input(indata, part=part)
    return min(traverse(seed, maps, part) for seed in seeds)


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split("/")[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n\n")

    part1_answer = solve(puzzle_input, part="a")
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = solve(puzzle_input, part="b")
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
