#  18   01:03:09   3516      0   01:47:47   2271      0

from aocd.models import Puzzle


def solve(instructions):
    y = x = area = 0
    for dirr, length in instructions:
        new_y = y + length if dirr == "D" else y - length if dirr == "U" else y
        new_x = x + length if dirr == "R" else x - length if dirr == "L" else x
        area += x * new_y - y * new_x + length  # shoelace formula
        y, x = new_y, new_x
    return area // 2 + 1


def part1(indata):
    instructions = [(row.split()[0], int(row.split()[1])) for row in indata]
    return solve(instructions)


def part2(indata):
    instructions = []

    for row in indata:
        instr = row.split("#")[1].split(")")[0]
        length = int(instr[:-1], 16)
        dirr = "RDLU"[int(instr[-1])]
        instructions.append((dirr, length))

    return solve(instructions)


if __name__ == "__main__":
    puzzle = Puzzle(day=18, year=2023)
    puzzle_input = puzzle.input_data.split("\n")
    print(f"\npart1: {part1(puzzle_input)}\npart2: {part2(puzzle_input)}")
