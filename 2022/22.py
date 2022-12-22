# 22   01:34:14   2612      0   06:46:30   2557      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2022, 22

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n\n')
input_grid = indata[0].split('\n')

CUBE_SIZE = 50
HEIGHT = len(input_grid)
WIDTH = max(len(row) for row in input_grid)

grid = [[input_grid[y][x] if x < len(input_grid[y]) else ' ' for x in range(WIDTH)] for y in range(HEIGHT)]
moves = indata[1].replace('L', ' L ').replace('R', ' R ').split(' ')

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_symbol = ['>', 'v', '<', '^']

above = { 1:(6,0,'x',0), 2:(6,3,-1,'x'), 3:(1,3,-1,'x'), 4:(3,0,'x',0), 5:(3,3,-1,'x'), 6:(4,3,-1,'x') }
below = { 1:(3,1,0,'x'), 2:(3,2,'x',-1), 3:(5,1,0,'x'), 4:(6,1,0,'x'), 5:(6,2,'x',-1), 6:(2,1,0,'x')}
left =  { 1:(4,0,'my',0), 2:(1,2,'y',-1), 3:(4,1,0,'y'), 4:(1,0,'my',0), 5:(4,2,'y',-1), 6:(1,1,0,'y')}
right = { 1:(2,0,'y',0), 2:(5,2,'my',-1), 3:(2,3,-1,'y'), 4:(5,0,'y',0), 5:(2,2,'my',-1), 6:(5,3,-1,'y')}


def cube2grid(pos):
  y, x, cube_side = pos
  match cube_side:
    case 1: return (y, x + CUBE_SIZE)
    case 2: return (y, x + CUBE_SIZE * 2)
    case 3: return (y + CUBE_SIZE, x + CUBE_SIZE)
    case 4: return (y + CUBE_SIZE * 2, x)
    case 5: return (y + CUBE_SIZE * 2, x + CUBE_SIZE)
    case 6: return (y + CUBE_SIZE * 3, x)


def move1(pos, dir):
  dy, dx = directions[dir]
  old_pos = pos[:]
  while True:
    pos = ((pos[0]+dy)%HEIGHT, (pos[1]+dx)%WIDTH)
    if grid[pos[0]][pos[1]] != ' ':
      break
  if grid[pos[0]][pos[1]] == '#':
    return old_pos
  else:
    return pos


def move2(old_pos, dir):
  dy, dx = directions[dir]
  new_pos = (old_pos[0]+dy, old_pos[1]+dx, old_pos[2])

  if 0 <= new_pos[0] < CUBE_SIZE and 0 <= new_pos[1] < CUBE_SIZE:
    grid_y, grid_x = cube2grid(new_pos)
    if grid[grid_y][grid_x] != '#':
      return new_pos, dir
    else:
      return old_pos, dir
  
  if   new_pos[0] < 0:          cube_data = above[old_pos[2]]
  elif new_pos[0] >= CUBE_SIZE: cube_data = below[old_pos[2]]
  elif new_pos[1] < 0:          cube_data =  left[old_pos[2]]
  elif new_pos[1] >= CUBE_SIZE: cube_data = right[old_pos[2]]

  new_pos = [new_pos[0], new_pos[1], cube_data[0]]
  new_dir = cube_data[1]

  for i, change in enumerate(cube_data[2:]):
    match change:
      case   -1: new_pos[i] = CUBE_SIZE - 1
      case    0: new_pos[i] = 0
      case  'y': new_pos[i] = old_pos[0]
      case  'x': new_pos[i] = old_pos[1]
      case 'my': new_pos[i] = (CUBE_SIZE-1) - old_pos[0]
      case 'mx': new_pos[i] = (CUBE_SIZE-1) - old_pos[1]
  
  new_pos = tuple(new_pos)

  grid_y, grid_x = cube2grid(new_pos)
  if grid[grid_y][grid_x] != '#':
    return new_pos, new_dir
  else:
    return old_pos, dir


def solve():
  pos1 = (0, grid[0].index('.'))
  pos2 = (0, 0, 1) # (y, x, cube side)
  dir1 = dir2 = 0
  for move in moves:
    if move == 'L':
      dir1 = (dir1 - 1) % 4
      dir2 = (dir2 - 1) % 4
    elif move == 'R':
      dir1 = (dir1 + 1) % 4
      dir2 = (dir2 + 1) % 4
    else:
      for _ in range(int(move)):
        pos1 = move1(pos1, dir1)
        pos2, dir2 = move2(pos2, dir2)

  pos2 = cube2grid(pos2)
  p1_answer = 1000 * (pos1[0]+1) + 4 * (pos1[1]+1) + dir1
  p2_answer = 1000 * (pos2[0]+1) + 4 * (pos2[1]+1) + dir2
  return p1_answer, p2_answer


if __name__ == "__main__":
  t0 = time.time()
  p1_answer, p2_answer = solve()
  submit(p1_answer, part="a", day=DAY, year=YEAR)
  submit(p2_answer, part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)