import time

from aocd.models import Puzzle
YEAR, DAY = 2015, 8
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')


def part1():
  result = 0
  for row in indata:
    escaped_string = row.encode().decode('unicode-escape')
    result += 2 + len(row) - len(escaped_string)
  return result

def part2():
  result = 0
  for string in indata:
    result += 2
    for char in string:
      if char == '"' or char == '\\':
        result += 1
  return result

if __name__ == "__main__":
  t0 = time.time()
  print("part1:", part1())
  print("part2:", part2())
  print("time:", time.time()-t0)
