#  5   00:33:24   3612      0   01:46:25   3724      0

from aocd.models import Puzzle
from aocd import submit
import re
import time


def parse_input(indata):
    initial_seeds = [('seed', int(x)) for x in re.findall(r"\d+", indata[0])]
    maps = {}
    for mapp in indata[1:]:
        mapp = mapp.split("\n")
        source, dest = mapp[0].split(' ')[0].split('-to-')
        x = [dest]
        for row in mapp[1:]:
            dest_range, source_range, range_length = [int(x) for x in re.findall(r"\d+", row)]
            x.append((dest_range, source_range, range_length))
        maps[source] = x
    return initial_seeds, maps


def get_next_seed(category, number, maps):
    dest = maps[category][0]
    res = []
    for i0, i1, length in maps[category][1:]:
        if i1 <= number < i1+length:
            res.append((dest, i0 + (number - i1)))
    return res or [(dest, number)]


def overlaps(a0, a1, b0, b1):
    overlap = None
    non_overlap = []
    # a: [   ]
    # b:   [ ...
    if a0 <= b0 < a1:
        overlap = (b0, min(a1, b1))

    # a:   [ ...
    # b: [   ]
    if b0 <= a0 < b1:
        overlap = (a0, min(a1, b1))

    # a: [   ]
    # b:       [   ]
    if a1 <= b0 or b1 <= a0:
        non_overlap += [(a0, a1)]

    # a: [   ]
    # b:  [   ]
    if a0 < b0 < a1 < b1:
        non_overlap += [(a0, b0)]

    # a:  [   ]
    # b: [   ]
    elif b0 < a0 < b1 < a1:
        non_overlap += [(b1, a1)]

    # a: [     ]
    # b:  [   ]
    elif a0 < b0 < b1 < a1:
        non_overlap += [(a0, b0), (b1, a1)]
    
    return overlap, non_overlap



def get_next_range(category, r0, r1, maps):
    dest = maps[category][0]
    res = []
    ranges = [(r0, r1)]
    for d, s, l in maps[category][1:]:
        new_ranges = []
        for r0, r1 in ranges:
            overlap, non_overlap = overlaps(r0, r1, s, s+l)
            if overlap:
                a, b = overlap
                res += [(dest, a-s+d, b-s+d)]
            new_ranges += non_overlap
        ranges = new_ranges

    # leftover ranges
    for non_overlap in ranges:
        a, b = non_overlap
        res += [(dest, a, b)]

    return res


def part1(indata):
    seeds, maps = parse_input(indata)

    locations = []
    while seeds:
        category, number = seeds.pop()
        if category == 'location':
            locations.append(number)
            continue
        seeds += get_next_seed(category, number, maps)
    return min(locations)


def part2(indata):
    seed_ranges, maps = parse_input(indata)

    seeds = []
    i = 0
    while i < len(seed_ranges):
        start = seed_ranges[i][1]
        length = seed_ranges[i+1][1]
        seeds.append(('seed', start, start+length))
        i += 2

    locations = []
    while seeds:
        category, a, b = seeds.pop()
        if category == 'location':
            locations.append(a)
            continue
        seeds += get_next_range(category, a, b, maps)
    return min(locations)


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n\n")
    example_input = puzzle.examples[0].input_data.split("\n\n")

    ex1 = part1(example_input)
    ex1_answer = int(puzzle.examples[0].answer_a)
    assert ex1 == ex1_answer, f"Ex1: expected {ex1_answer}, got {ex1}"

    part1_answer = part1(puzzle_input)
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2(puzzle_input)
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)
        
    print("\ntime:", time.time()-t0)