import os
import getch

indata = \
"""        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""".split('\n\n')

input_grid = indata[0].split('\n')

CUBE_SIZE = 4
HEIGHT = len(input_grid)
WIDTH = max(len(row) for row in input_grid)

grid = [[input_grid[y][x] if x < len(input_grid[y]) else ' ' for x in range(WIDTH)] for y in range(HEIGHT)]
moves = indata[1].replace('L', ' L ').replace('R', ' R ').split(' ')

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_symbol = ['>', 'v', '<', '^']

above = { 1:(2,1, 0,'mx'), 2:(1,1, 0,'mx'), 3:(1,0,'x', 0), 4:(1,3,-1,'x'), 5:(4,3,-1, 'x'), 6:(4,2,'mx',-1) }
below = { 1:(4,1, 0, 'x'), 2:(5,3,-1,'mx'), 3:(5,0,'mx',0), 4:(5,1, 0,'x'), 5:(2,3,-1,'mx'), 6:(2,0,'mx', 0) }
left  = { 1:(3,1, 0, 'y'), 2:(6,3,-1,'my'), 3:(2,2,'y',-1), 4:(3,2,'y',-1), 5:(3,3,-1,'my'), 6:(5,2,'y', -1) }
right = { 1:(6,2,'my',-1), 2:(3,0, 'y', 0), 3:(4,0,'y', 0), 4:(6,1,0,'my'), 5:(6,0, 'y', 0), 6:(1,2,'my',-1) }


def cube2grid(pos):
  y, x, cube_side = pos
  match cube_side:
    case 1: return (y, x + CUBE_SIZE * 2)
    case 2: return (y + CUBE_SIZE, x)
    case 3: return (y + CUBE_SIZE, x + CUBE_SIZE)
    case 4: return (y + CUBE_SIZE, x + CUBE_SIZE * 2)
    case 5: return (y + CUBE_SIZE * 2, x + CUBE_SIZE * 2)
    case 6: return (y + CUBE_SIZE * 2, x + CUBE_SIZE * 3)


def print_cube(pos, dir):
  os.system('clear')
  grid_y, grid_x = cube2grid(pos)
  for y in range(HEIGHT):
    row = ""
    for x in range(WIDTH):
      if (y, x) == (grid_y, grid_x):
        row += dir_symbol[dir]
      else:
        row += grid[y][x]
    print(row)


def move(old_pos, dir):
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


def interactive_cube():
  pos = (0, 0, 1) # (y, x, cube_side)
  dir = 0
  while True:
    print_cube(pos, dir)
    match getch.getch():
      case 'a':
        dir = (dir - 1) % 4
        continue
      case 'd':
        dir = (dir + 1) % 4
        continue
      case _: 
        pos, dir = move(pos, dir)


if __name__ == "__main__":
  interactive_cube()