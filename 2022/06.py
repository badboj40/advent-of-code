#  6   00:06:43   3527      0   00:07:32   2889      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR = int('2022')
DAY = int('06')

def parse_input():
  puzzle = Puzzle(day=DAY, year=YEAR)
  indata = puzzle.input_data
  return indata


def part1(indata):
  for i in range(len(indata)):
    if len(set(indata[i:i+4])) == 4:
      return i+4
  return -1


def part2(indata):
  for i in range(len(indata)):
    if len(set(indata[i:i+14])) == 14:
      return i+14
  return -1


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
