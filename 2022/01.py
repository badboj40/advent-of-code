from aocd.models import Puzzle
import time

def parse_input():
  puzzle = Puzzle(2022, int("01"))
  indata = puzzle.input_data.split('\n')
  return indata

def part1(indata):
  calories = []
  cals = 0
  for row in indata:
    if row:
      cals += int(cals)
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
  print() 
  indata = parse_input()
  t0 = time.time()
  
  print("part1:", part1(indata))
  print("part2:", part2(indata))

  print("time:", time.time()-t0)
