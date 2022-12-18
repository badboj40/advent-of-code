# 18   00:18:59   2453      0   01:02:06   2108      0

from aocd.models import Puzzle
from aocd import submit
import re
import time

YEAR, DAY = 2022, 18

puzzle = Puzzle(day=DAY, year=YEAR)
indata = {tuple(int(d) for d in re.findall(r"\d+", row)) for row in puzzle.input_data.split("\n")}

exterior_air = set()
LAVA_SIZE = 20 # (min, max) for x, y, z in my indata (0, 19), (1, 19),  (1, 18)


def get_neighbors(x, y, z):
  return {(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)}


def dfs(x, y, z, visited=None):
  if visited is None: visited = set()
  if (x, y, z) in exterior_air: return 1
  if (x, y, z) in visited or (x, y, z) in indata: return 0
  if x < 0 or x > LAVA_SIZE or y < 0 or y > LAVA_SIZE or z < 0 or z > LAVA_SIZE: return 1
  visited.add((x, y, z))
  for nx, ny, nz in get_neighbors(x, y, z):
    if dfs(nx, ny, nz, visited):
      exterior_air.add((nx, ny, nz))
      return 1
  return 0


def area(x, y, z):
  return len(get_neighbors(x, y, z) - indata)


def exterior_area(x, y, z):
  return sum(dfs(nx, ny, nz) for nx, ny, nz in get_neighbors(x, y, z))


def solve():
  score1 = score2 = 0
  for x, y, z in indata:
    score1 += area(x, y, z)
    score2 += exterior_area(x, y, z)
  return score1, score2


if __name__ == "__main__":
  t0 = time.time()
  part1_answer, part2_answer = solve()
  submit(part1_answer, part="a", day=DAY, year=YEAR)
  submit(part2_answer, part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)