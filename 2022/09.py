from aocd.models import Puzzle
from aocd import submit
import numpy as np
import math
import time

YEAR = int('2022')
DAY = int('09')

puzzle = Puzzle(day=DAY, year=YEAR)

convert_dir = {
  'R':( 0, 1),
  'L':( 0,-1),
  'U':(-1, 0),
  'D':( 1, 0),
}

indata = [
  (convert_dir[row.split(' ')[0]], int(row.split(' ')[1]))
  for row in puzzle.input_data.split('\n')
]


def handle_step1(head, tail, dir):
  head = np.add(head, dir)
  x_diff, y_diff = np.subtract(head, tail)
  if abs(x_diff) == 2:
    tail = tail[0] + x_diff/2, head[1]
  elif abs(y_diff) == 2:
    tail = head[0], tail[1] + y_diff/2
  return head, tail


def part1():
  visited_by_tail = set()
  head = tail = (0, 0)
  for dir, steps in indata:
    for _ in range(steps):
      visited_by_tail.add(tail)
      head, tail = handle_step1(head, tail, dir)
  return len(visited_by_tail)


def handle_step2(rope, dir):
  rope[0] = np.add(rope[0], dir)
  for i in range(1, len(rope)):
    head_x, head_y = rope[i-1]
    tail_x, tail_y = rope[i]
    x_diff, y_diff = np.subtract(rope[i-1], rope[i])
    if abs(x_diff) == abs(y_diff) == 2:
      rope[i] = tail_x + x_diff/2 , tail_y + y_diff/2
    elif abs(x_diff) == 2:
      rope[i] = tail_x + x_diff/2, head_y
    elif abs(y_diff) == 2:
      rope[i] = head_x, tail_y + y_diff/2
  return rope


def part2():
  visited_by_tail = set()
  rope = [(0, 0)] * 10
  for dir, steps in indata:
    for _ in range(steps):
      rope = handle_step2(rope, dir)
      visited_by_tail.add(rope[-1])
  return len(visited_by_tail)


if __name__ == "__main__":
  t0 = time.time()

  part1_answer = part1()
  print("\npart1:", part1_answer)
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2()
  print("\npart2:", part2_answer)
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)
