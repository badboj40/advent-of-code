# 12   00:41:22   3022      0   00:47:54   2874      0

from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time

YEAR = int('2022')
DAY = int('12')

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')

alphabet = "abcdefghijklmnopqrstuvwxyz"


def parse_indata():
  heightmap = []
  start = goal = (0, 0)
  for y, row in enumerate(indata):
    map_row = []
    for x, char in enumerate(row):
      if char in alphabet:
        map_row.append(alphabet.find(char))
      elif char == 'S':
        map_row.append(alphabet.find('a'))
        start = (y, x)
      elif char == 'E':
        map_row.append(alphabet.find('z'))
        goal = (y, x)
    heightmap.append(map_row)
  return start, goal, heightmap


def get_neighbors(y, x, heightmap, parents):
  neighbors = []
  if y-1 >= 0 and (y-1, x) not in parents and heightmap[y-1][x] <= heightmap[y][x]+1:
    neighbors.append((y-1, x))
    parents[(y-1, x)] = (y, x)
  if x-1 >= 0 and (y, x-1) not in parents and heightmap[y][x-1] <= heightmap[y][x]+1:
    neighbors.append((y, x-1))
    parents[(y, x-1)] = (y, x)
  if y+1 < len(heightmap) and (y+1, x) not in parents and heightmap[y+1][x] <= heightmap[y][x]+1:
    neighbors.append((y+1, x))
    parents[(y+1, x)] = (y, x)
  if x+1 < len(heightmap[y]) and (y, x+1) not in parents and heightmap[y][x+1] <= heightmap[y][x]+1:
    neighbors.append((y, x+1))
    parents[(y, x+1)] = (y, x)
  return neighbors


def BFS(start, goal, heightmap):
  queue = [start]
  parents = dict()
  steps = 0
  while queue:
    position = queue.pop(0)
    if position == goal:
      steps = 1
      while parents[position] != start:
        steps += 1
        position = parents[position]
      return steps
    queue += get_neighbors(position[0], position[1], heightmap, parents)
  # path not found
  return float('inf')


def part1():
  start, goal, heightmap = parse_indata()
  return BFS(start, goal, heightmap)


def part2():
  start, goal, heightmap = parse_indata()
  steps = []
  for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
      if heightmap[y][x] == 0:
        start = (y, x)
        steps.append(BFS(start, goal, heightmap))
  return min(steps)


if __name__ == "__main__":
  t0 = time.time()

  part1_answer = part1()
  print("\npart1:", part1_answer)
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2()
  print("\npart2:", part2_answer)
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)
