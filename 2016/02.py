from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2016, 2
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')

n1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

n2 = [[0,   0,   1,   0,   0],
      [0,   2,   3,   4,   0],
      [5,   6,   7,   8,   9],
      [0,  'A', 'B', 'C',  0],
      [0,   0,  'D',  0,   0]]


def part1():
    y, x = 1, 1
    result = ""
    for instruction in indata:
        for d in instruction:
            if d == 'L' and x-1 >= 0: x -= 1
            if d == 'R' and x+1 <= 2: x += 1
            if d == 'U' and y-1 >= 0: y -= 1
            if d == 'D' and y+1 <= 2: y += 1
        result += str(n1[y][x])
    return result


def part2():
    y, x = 2, 0
    result = ""
    for instruction in indata:
        for d in instruction:
            if d == 'L' and x-1 >= 0 and n2[y][x-1]: x -= 1
            if d == 'R' and x+1 <= 4 and n2[y][x+1]: x += 1
            if d == 'U' and y-1 >= 0 and n2[y-1][x]: y -= 1
            if d == 'D' and y+1 <= 4 and n2[y+1][x]: y += 1
        result += str(n2[y][x])
    return result


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
