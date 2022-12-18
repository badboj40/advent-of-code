from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time

YEAR, DAY = 2015, 16

real_aunt = {
  "children": 3,
  "cats": 7,
  "samoyeds": 2,
  "pomeranians": 3,
  "akitas": 0,
  "vizslas": 0,
  "goldfish": 5,
  "trees": 3,
  "cars": 2,
  "perfumes": 1,
}

def parse_input():
  puzzle = Puzzle(day=DAY, year=YEAR)
  indata = puzzle.input_data.split('\n')
  aunts = []
  for row in indata:
    aunt = {}
    i = row.find(':') + 2
    for pair in row[i:].split(','):
      attribute = pair.strip().split(' ')[0][:-1]
      amount = int(pair.strip().split(' ')[1])
      aunt[attribute] = amount
    aunts.append(aunt)
  return aunts


def part1(indata):
  for i, aunt in enumerate(indata):
    for attribute in aunt:
      if aunt[attribute] != real_aunt[attribute]:
        break
    else:
      return i + 1
  return -1


def part2(indata):
  for i, aunt in enumerate(indata):
    for attribute in aunt:
      match attribute:
        case 'cats' | 'trees':
          if not (aunt[attribute] > real_aunt[attribute]): break
        case 'pomeranians' | 'goldfish':
          if not (aunt[attribute] < real_aunt[attribute]): break
        case _:
          if not (aunt[attribute] == real_aunt[attribute]): break
    else:
      return i + 1
  return -1


if __name__ == "__main__":
  indata = parse_input()
  t0 = time.time()
  submit(part1(indata), part="a", day=DAY, year=YEAR)
  submit(part2(indata), part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)
