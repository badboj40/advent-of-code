from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2016, 3

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')


def part1():
    count = 0
    for triangle in indata:
        a, b, c = map(int, triangle.split())
        count += a+b>c and a+c>b and b+c>a
    return count


def part2():
    count = 0
    triangles = [tuple(map(int, triangle.split())) for triangle in indata]
    for i in range(0, len(triangles), 3):
        for col in range(3):
            a, b, c = triangles[i][col], triangles[i+1][col], triangles[i+2][col]
            count += a+b>c and a+c>b and b+c>a
    return count


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
