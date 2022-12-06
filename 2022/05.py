from aocd.models import Puzzle
from aocd import submit
import numpy as np
from copy import deepcopy
import time

YEAR = int('2022')
DAY = int('05')


def parse_input():
  puzzle = Puzzle(day=DAY, year=YEAR)
  stack, instructions = (x.split('\n') for x in puzzle.input_data.split('\n\n'))

  stacks = []
  for i in range(9):
    stacks.append([])

  for row in reversed(stack[:-1]):
    for i in range(9):
      block = row[4*i + 1]
      if block != ' ':
        stacks[i].append(block)
  return stacks, instructions


def part1(indata):
  stacks, instructions = deepcopy(indata)
  for instruction in instructions:
    amount = int(instruction.split(' ')[1])
    move_from = int(instruction.split(' ')[3]) - 1
    move_to = int(instruction.split(' ')[5]) - 1
    for i in range(amount):
      block = stacks[move_from].pop()
      stacks[move_to].append(block)
    pass
  
  result = ''
  for stack in stacks:
    result += stack[-1]

  return result


def part2(indata):
  stacks, instructions = deepcopy(indata)
  for instruction in instructions:

    amount = int(instruction.split(' ')[1])
    move_from = int(instruction.split(' ')[3]) - 1
    move_to = int(instruction.split(' ')[5]) - 1

    stacks[move_to] += stacks[move_from][-amount:]
    stacks[move_from] = stacks[move_from][:-amount]

  result = ''
  for stack in stacks:
    if stack:
      result += stack[-1]
  return result


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
