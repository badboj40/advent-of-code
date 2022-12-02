from aocd.models import Puzzle
from aocd import submit
import time

YEAR = int('2022')
DAY = int('01')

def parse_input():
  puzzle = Puzzle(day=DAY, year=YEAR)
  indata = puzzle.input_data.split('\n')
  return indata


def part1(indata):
  calories = []
  cals = 0
  for row in indata:
    if row:
      cals += int(row)
    else:
      calories.append(cals)
      cals = 0
  return max(calories)


def part2(indata):
  calories = []
  cals = 0
  for row in indata:
    if row:
      cals += int(row)
    else:
      calories.append(cals)
      cals = 0
  calories.sort()
  return sum(calories[-3:])


if __name__ == "__main__":
  indata = parse_input()
  t0 = time.time()

  part1_answer = part1(indata)
  print("\npart1:", part1(indata))
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2(indata)
  print("\npart2:", part2(indata))
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)
