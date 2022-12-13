# 13   00:31:45   2073      0   00:48:11   2458      0

from aocd.models import Puzzle
from aocd import submit
import time
import ast
from functools import cmp_to_key


YEAR = int('2022')
DAY = int('13')

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n\n')

def compare(left, right):
  if isinstance(left, int) and isinstance(right, int):
    return right - left
  elif isinstance(left, list) and isinstance(right, list):
    left = left.copy()
    right = right.copy()
    while left and right:
      result = compare(left.pop(0), right.pop(0))
      if result != 0:
        return result
    return int(not left) - int(not right)
  else: # one int and one list
    if isinstance(right, int) : right = [right]
    elif isinstance(left, int): left = [left]
    return compare(left, right)


def part1():
  score = 0
  for i, pair in enumerate(indata):
    left, right = [ast.literal_eval(x) for x in pair.split('\n')]
    if compare(left, right) > 0:
      score += i+1
  return score


def part2():
  packets = [[2], [6]]
  for pair in indata:
    left, right = [ast.literal_eval(x) for x in pair.split('\n')]
    packets += [left, right]
  packets.sort(key=cmp_to_key(compare), reverse=True)

  return (packets.index([2]) + 1) * (packets.index([6]) + 1)


if __name__ == "__main__":
  t0 = time.time()

  part1_answer = part1()
  print("\npart1:", part1_answer)
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2()
  print("\npart2:", part2_answer)
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)
