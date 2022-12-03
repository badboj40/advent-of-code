from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time

YEAR = int('2022')
DAY = int('03')

def parse_input():
  puzzle = Puzzle(day=DAY, year=YEAR)
  indata = puzzle.input_data.split('\n')
  return indata


alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1(indata):
  score = 0
  for row in indata:
    first = row[:int(len(row)/2)]
    second = row[int(len(row)/2):]
    for char in first:
      if char in second:
        score += alphabet.find(char)
        break
  return score


def part2(indata):
  score = 0
  i = 0
  while i < len(indata):
    first, second, third = indata[i:i+3]
    for char in first:
      if char in second and char in third:
        score += alphabet.find(char)
        break
    i += 3
  return score


if __name__ == "__main__":
  indata = parse_input()
  t0 = time.time()

  part1_answer = part1(indata)
  print("\npart1:", part1(indata))
  # submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2(indata)
  print("\npart2:", part2(indata))
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)
