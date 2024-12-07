#  7   00:06:43   749      0   00:09:18   644      0

from aocd.models import Puzzle
import re
import time


def calc(answer, current, numbers, part2=False):
    if not numbers:
        return answer == current
    if current > answer:
        return False
    n, *numbers = numbers
    results = [current * n, current + n]
    if part2:
        results.append(int(str(current)+str(n)))
    return any(calc(answer, res, numbers, part2) for res in results)


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    indata = [[*map(int,re.findall(r'\d+', row))] for row in puzzle.input_data.split('\n')]

    p1 = sum(row[0] for row in indata if calc(row[0], row[1], row[2:]))
    p2 = sum(row[0] for row in indata if calc(row[0], row[1], row[2:], True))

    print("\npart1:", p1)
    print("\npart2:", p2)
    print("\ntime:", time.time()-t0)