#  8   00:19:13   2958      0   00:47:10   4650      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR = int('2022')
DAY = int('08')

def parse_input():
  puzzle = Puzzle(day=DAY, year=YEAR)
  indata = puzzle.input_data.split('\n')
  return indata


def part1(indata):
  visible_trees = set()
  for y in range(len(indata)): # left to right
    highest_tree = -1
    for x in range(len(indata[0])):
      tree_height = int(indata[y][x])
      if tree_height > highest_tree:
        visible_trees.add((y, x))
        highest_tree = tree_height

  for y in range(len(indata)): # right to left
    highest_tree = -1
    for x in reversed(range(len(indata[0]))):
      tree_height = int(indata[y][x])
      if tree_height > highest_tree:
        visible_trees.add((y, x))
        highest_tree = tree_height
  
  for x in range(len(indata)): # downwards
    highest_tree = -1
    for y in range(len(indata[0])):
      tree_height = int(indata[y][x])
      if tree_height > highest_tree:
        visible_trees.add((y, x))
        highest_tree = tree_height
  
  for x in range(len(indata)): # upwards
    highest_tree = -1
    for y in reversed(range(len(indata[0]))):
      tree_height = int(indata[y][x])
      if tree_height > highest_tree:
        visible_trees.add((y, x))
        highest_tree = tree_height

  return len(visible_trees)


def part2(indata):
  best_scenic_score = 0
  for y in range(1, len(indata)-1):
    for x in range(1, len(indata[0])-1):
      tree_height = int(indata[y][x])
      scenic_score = i = 1
      left_to_right = right_to_left = downwards = upwards = True

      while left_to_right or right_to_left or downwards or upwards:
        if left_to_right and (tree_height <= int(indata[y][x+i]) or x+i == len(indata[0])-1):
          scenic_score *= i
          left_to_right = False

        if right_to_left and (tree_height <= int(indata[y][x-i]) or x-i == 0):
          scenic_score *= i
          right_to_left = False

        if downwards and (tree_height <= int(indata[y+i][x]) or y+i == len(indata)-1):
          scenic_score *= i
          downwards = False

        if upwards and (tree_height <= int(indata[y-i][x]) or y-i == 0):
          scenic_score *= i
          upwards = False
        i += 1
      best_scenic_score = max(scenic_score, best_scenic_score)
  return best_scenic_score


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
