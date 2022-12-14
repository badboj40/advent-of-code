#  14   00:50:23   3791      0   01:34:09   5477      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR = int('2022')
DAY = int('14')

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')


X_MIN = min([min([int(node.split(',')[0]) for node in line.split(' -> ')]) for line in indata])
X_MAX = max([max([int(node.split(',')[0]) for node in line.split(' -> ')]) for line in indata])
Y_MAX = max([max([int(node.split(',')[1]) for node in line.split(' -> ')]) for line in indata])


def generate_cave():
  cave = dict()
  for line in indata:
    nodes = [[int(b) for b in a.split(',')] for a in line.split(' -> ')]
    for i in range(len(nodes) - 1):
      x0, y0 = nodes[i]
      x1, y1 = nodes[i+1]
      x = min(x0, x1)
      y = min(y0, y1)

      for dx in range(abs(x0 - x1) + 1):
        cave[x+dx, y] = '#'
      for dy in range(abs(y0 - y1) + 1):
        cave[x, y+dy] = '#'

  for x in range(-10000, 10000):
    cave[x, Y_MAX+2] = '#'
  return cave


def print_cave(cave):
  for y in range(Y_MAX+2):
    row = ""
    for x in range(X_MIN-10, X_MAX+11):
      if (x, y) in cave:
        row += cave[(x, y)]
      else:
        row += '.'
    print(row)
  print()


def spawn_sand(cave, part1):
  sandx, sandy = (500, 0)
  
  if (sandx, sandy) in cave: # Sand spawn covered by sand in part 2
    return False

  while True:
    if part1 and sandy == Y_MAX: # Fell off during part 1
      return False

    sandy += 1
    if (sandx,   sandy) not in cave: cave[(sandx,   sandy)] = '.'
    if (sandx-1, sandy) not in cave: cave[(sandx-1, sandy)] = '.'
    if (sandx+1, sandy) not in cave: cave[(sandx+1, sandy)] = '.'
    
    if   cave[(sandx,   sandy)] == '.': pass
    elif cave[(sandx-1, sandy)] == '.': sandx -= 1
    elif cave[(sandx+1, sandy)] == '.': sandx += 1
    else: break

  cave[(sandx, sandy-1)] = 'o'
  return True


def part1(cave):
  while spawn_sand(cave, part1=True): pass
  return sum(x == 'o' for x in cave.values())


def part2(cave):
  while spawn_sand(cave, part1=False): pass
  return sum(x == 'o' for x in cave.values())


if __name__ == "__main__":
  t0 = time.time()
  
  cave = generate_cave()

  # Part 1
  while spawn_sand(cave, part1=True): pass
  part1_answer = sum(x == 'o' for x in cave.values())
  print("\npart1:", part1_answer)
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  # Part 2
  while spawn_sand(cave, part1=False): pass
  part2_answer = sum(x == 'o' for x in cave.values())
  print("\npart2:", part2_answer)
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)