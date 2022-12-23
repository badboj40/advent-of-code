#  6   00:06:43   3527      0   00:07:32   2889      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2022, 6
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data


def solve(length):
  for i in range(len(indata)):
    if len(set(indata[i:i+length])) == length:
      return i+length


if __name__ == "__main__":
  t0 = time.time()
  submit(solve(4), part="a", day=DAY, year=YEAR)
  submit(solve(14), part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)