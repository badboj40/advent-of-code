# 15   02:09:14   7078      0   02:33:26   4189      0

from aocd.models import Puzzle
from aocd import submit
import re
import time

YEAR, DAY = 2022, 15
puzzle = Puzzle(day=DAY, year=YEAR)
indata = [[int(d) for d in re.findall(r"-?\d+", row)] for row in puzzle.input_data.split('\n')]

sensors = {(sx, sy) : abs(sx-bx) + abs(sy-by) for sx, sy, bx, by in indata}
beacons = {(bx, by) for _, _, bx, by in indata}


def merge_intervals(intervals):
  intervals.sort(key=lambda x: x[0])
  merged = []
  for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
      merged.append(interval)
    else:
      merged[-1][1] = max(merged[-1][1], interval[1])
  return merged 


def solve():
  part1_answer = part2_answer = 0
  for y in range(int(4e6+1)):
    intervals = []
    for sx, sy in sensors:
      coverage = sensors[(sx, sy)] - abs(sy - y)
      if coverage >= 0:
        intervals.append([sx-coverage, sx+coverage])
    merged = merge_intervals(intervals)
    if y == 2e6: # part 1
      part1_answer = sum([interval[1] - interval[0] for interval in merged])
    if len(merged) > 1: # part 2
      part2_answer = int((merged[0][1]+1) * 4e6 + y)
      break
  return part1_answer, part2_answer


if __name__ == "__main__":
  t0 = time.time()
  part1_answer, part2_answer = solve()
  submit(part1_answer, part="a", day=DAY, year=YEAR)
  submit(part2_answer, part="b", day=DAY, year=YEAR)
  print(f"time: {time.time()-t0}")