# 23   01:11:22   1932      0   01:21:42   1947      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2022, 23

puzzle = Puzzle(day=DAY, year=YEAR)
indata = [[char for char in row] for row in puzzle.input_data.split('\n')]


def make_decision(elf, elves, i):
  y, x = elf
  neighbors = sum((y+dy, x+dx) in elves for dy in range(-1, 2) for dx in range(-1, 2)) - 1
  if not neighbors:
    return
  north = [(y-1, x+dx) for dx in range(-1, 2)]
  south = [(y+1, x+dx) for dx in range(-1, 2)]
  west =  [(y+dy, x-1) for dy in range(-1, 2)]
  east =  [(y+dy, x+1) for dy in range(-1, 2)]
  directions = [north,south,west,east][i%4:] + [north,south,west,east][:i%4]
  for dir in range(4):
    if all(coord not in elves for coord in directions[dir]):
      elves[elf] = directions[dir][1]
      return


def move(elves):
  new_positions = set()
  duplicate_positions = set()
  for position in elves.values():
    if position in new_positions:
      duplicate_positions.add(position)
    else:
      new_positions.add(position)
  
  for elf, new_position in elves.items():
    if new_position in duplicate_positions:
      elves[elf] = elf
    
  new_elves = {new_position : new_position for elf, new_position in elves.items()}
  return new_elves


def get_score(elves):
  score = 0
  for y in range(min(y for y,_ in elves), max(y for y,_ in elves) + 1):
    for x in range(min(x for _,x in elves), max(x for _,x in elves) + 1):
      if (y, x) not in elves:
        score += 1
  return score


def solve():
  elves = {(y,x): (y,x) for x in range(len(indata[0])) for y in range(len(indata)) if indata[y][x] == '#'}
  i = 0
  while True:
    if i == 10:
      p1_answer = get_score(elves)
    for elf in elves:
      make_decision(elf, elves, i)
    new_elves = move(elves)
    if new_elves == elves:
      p2_answer = i + 1
      break
    elves = new_elves
    i += 1
  
  return p1_answer, p2_answer


if __name__ == "__main__":
  t0 = time.time()
  p1_answer, p2_answer = solve()
  print(p1_answer, p2_answer)
  submit(p1_answer, part="a", day=DAY, year=YEAR)
  submit(p2_answer, part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)