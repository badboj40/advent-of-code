from aocd.models import Puzzle
from aocd import submit
import re
import time

directory, filename = __file__.split('/')[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
y, x = map(int, re.findall(r'\d+', puzzle.input_data))

START_CODE = 20151125
GOAL_INDEX = (x + y - 1) * (x + y) // 2 - y + 1


def solve():
    code = START_CODE
    for i in range(GOAL_INDEX - 1):
        code = (code * 252533) % 33554393
    return code


if __name__ == "__main__":
    t0 = time.time()

    answer = solve()
    print("\nanswer:", answer)
    submit(answer, part="a", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
