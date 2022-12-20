import time
import json

from aocd.models import Puzzle
YEAR, DAY = 2015, 12
puzzle = Puzzle(day=DAY, year=YEAR)
indata = json.loads(puzzle.input_data)

def part1(document):
  result = 0
  if isinstance(document, int):
    result = document
  elif isinstance(document, list):
    result = sum(part1(item) for item in document)
  elif isinstance(document, dict):
    result = sum(part1(document[key]) for key in document)
  return result


def part2(document):
  if isinstance(document, int) or document == "red":
    return document
  result = 0
  if isinstance(document, list):
    for item in document:
      res = part2(item)
      if isinstance(res, int):
        result += res
  elif isinstance(document, dict):
    for key in document.keys():
      res = part2(document[key])
      if not isinstance(res, int):
        return 0
      result += res
  return result


if __name__ == "__main__":
  t0 = time.time()
  print("part1:", part1(indata))
  print("part2:", part2(indata))
  print("time:", time.time()-t0)
