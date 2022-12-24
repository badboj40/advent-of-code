# 24   01:20:14   1501      0   01:27:25   1352      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2022, 24

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')
WIDTH = len(indata[0])-1
HEIGHT = len(indata)-1


def move_blizzards(valley):
  new_valley = {}
  for pos, blizzards in valley.items():
    for blizzard in blizzards:
      match blizzard:
        case '>':
          new_pos = (pos[0], pos[1]+1) if pos[1]+1 < WIDTH else (pos[0], 1)
        case 'v':
          new_pos = (pos[0]+1, pos[1]) if pos[0]+1 < HEIGHT else (1, pos[1])
        case '<':
          new_pos = (pos[0], pos[1]-1) if pos[1]-1 >= 1 else (pos[0], WIDTH-1)
        case '^':
          new_pos = (pos[0]-1, pos[1]) if pos[0]-1 >= 1 else (HEIGHT-1, pos[1])
      if new_pos not in new_valley:
        new_valley[new_pos] = []
      new_valley[(new_pos)].append(blizzard)
  return new_valley


def bfs(start, goal, minute, valleys):
  cache = set()
  queue = [(start, minute+1)]
  while queue:
    pos, minute = queue.pop(0)
    if (pos, minute) in cache: continue
    cache.add((pos, minute))

    new_positions = [pos, (pos[0],pos[1]+1), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0]-1, pos[1])]
    if goal in new_positions:
      return minute

    for new_pos in new_positions:
      if (new_pos == pos or 0 < new_pos[0] < HEIGHT and 0 < new_pos[1] < WIDTH) and \
          new_pos not in valleys[minute%len(valleys)]:
        queue.append((new_pos, minute+1))
  return 0


def solve():
  valley = {(y,x):[indata[y][x]] for x in range(1,WIDTH) for y in range(1,HEIGHT) if indata[y][x] in '>v<^'}
  valleys = []
  # pre-calculate all possible valley states
  while valley not in valleys:
    valleys.append(valley)
    valley = move_blizzards(valley)

  start, goal = (0, 1), (HEIGHT, WIDTH - 1)
  t0 = 0
  t1 = bfs(start=start, goal=goal, minute=t0, valleys=valleys)
  t2 = bfs(start=goal, goal=start, minute=t1, valleys=valleys)
  t3 = bfs(start=start, goal=goal, minute=t2, valleys=valleys)
  return t1, t3


if __name__ == "__main__":
  t0 = time.time()
  p1_answer, p2_answer = solve()
  submit(p1_answer, part="a", day=DAY, year=YEAR)
  submit(p2_answer, part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)