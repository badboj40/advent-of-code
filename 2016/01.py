from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2016, 1
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split(', ')


def part1():
    y, x = 0, 0
    dy, dx = -1, 0
    for instruction in indata:
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == 'R':
            dy, dx = dx, -dy
        elif direction == 'L':
            dy, dx = -dx, dy
        y += dy * distance
        x += dx * distance
    return abs(y) + abs(x)


def part2():
    y, x = 0, 0
    dy, dx = -1, 0
    visited = set()
    for instruction in indata:
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == 'R':
            dy, dx = dx, -dy
        elif direction == 'L':
            dy, dx = -dx, dy
        for _ in range(1, distance+1):
            y += dy
            x += dx
            if (y, x) in visited:
                return abs(y) + abs(x)
            visited.add((y, x))


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
