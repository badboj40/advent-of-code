#  8   00:16:28  1839      0   00:23:03  1663      0

from aocd.models import Puzzle
import time


def get_antinodes(y, x, dy, dx, H, W):
    antinodes = []
    while 0 <= y < H and 0 <= x < W:
        antinodes += [(y, x)]
        y, x = y+dy, x+dx
    return antinodes
        

def solve(antennas, H, W):
    antinodes1, antinodes2 = set(), set()

    node_pairs = []
    for nodes in antennas.values():
        node_pairs += [(y1,x1,y2,x2) for y1,x1 in nodes for y2,x2 in nodes if (y1, x1) != (y2, x2)]

    for y1, x1, y2, x2 in node_pairs:
        antinodes = get_antinodes(y1, x1, y1-y2, x1-x2, H, W)
        antinodes1.update(antinodes[1:2])
        antinodes2.update(antinodes)

    return len(antinodes1), len(antinodes2)


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n")

    antennas = {}
    H, W = len(puzzle_input), len(puzzle_input[0])
    for y,row in enumerate(puzzle_input):
        for x, tile in enumerate(row):
            if tile != '.':
                antennas[tile] = antennas.get(tile, []) + [(y, x)]

    part1_answer, part2_answer = solve(antennas, H, W)

    print("\npart1:", part1_answer)
    print("\npart2:", part2_answer)
    print("\ntime:", time.time()-t0)