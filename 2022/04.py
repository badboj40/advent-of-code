from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time

YEAR = int('2022')
DAY = int('04')

def parse_input():
  puzzle = Puzzle(day=DAY, year=YEAR)
  indata = puzzle.input_data.split('\n')
  return indata


def part1(indata):
  score = 0
  for row in indata:
    a, b = row.split(',')
    a0, a1 = [int(x) for x in a.split('-')]
    b0, b1 = [int(x) for x in b.split('-')]
    if (a0 <= b0 and b1 <= a1) or (b0 <= a0 and a1 <= b1):
      score += 1

  return score


def part2(indata):
  score = 0
  for row in indata:
    a, b = row.split(',')
    a0, a1 = [int(x) for x in a.split('-')]
    b0, b1 = [int(x) for x in b.split('-')]
    if not (a1 < b0 or b1 < a0):
      score += 1

  return score


if __name__ == "__main__":
  indata = parse_input()
  t0 = time.time()

  part1_answer = part1(indata)
  print("\npart1:", part1_answer)
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2(indata)
  print("\npart2:", part2_answer)
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)
