# 17   01:51:37   2801      0   04:54:43   2761      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2022, 17

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data

WIDTH = 7

class Shape:
  def __init__(self, shape):
    self.x = 2
    self.y = 0
    match shape:
      case 0: self.shape = [[1, 1, 1, 1]]                     # -
      case 1: self.shape = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]  # +
      case 2: self.shape = [[0, 0, 1], [0, 0, 1], [1, 1, 1]]  # J
      case 3: self.shape = [[1], [1], [1], [1]]               # I
      case 4: self.shape = [[1, 1], [1, 1]]                   # #
    self.width = len(self.shape[0])
    self.height = len(self.shape)


def move(shape, direction, board):
  dx, dy = {'<':(-1, 0), '>':(1, 0), 'v':(0, 1)}[direction]
  # out of bounds check
  if shape.x+dx<0 or shape.x+shape.width+dx>WIDTH or shape.y+shape.height+dy>len(board):
    return False
  # collision check
  for y in range(shape.height):
    for x in range(shape.width):
      if shape.shape[y][x] > 0 and board[shape.y+y+dy][shape.x+x+dx] > 0:
        return False
  # move the piece
  shape.x += dx
  shape.y += dy
  return True


def add_to_board(shape, board):
  for y in range(shape.height):
    for x in range(shape.width):
      board[shape.y + y][shape.x + x] = max(shape.shape[y][x], board[shape.y+y][shape.x+x])


def part1(iterations):
  board = []

  indata_index = 0
  height_changes = []
  previous_height = 0
  for i in range(iterations):
    shape = Shape(i%5)
    board = [[0] * WIDTH for _ in range(3+shape.height)] + board

    while True:
      direction = indata[indata_index%len(indata)]
      indata_index += 1
      move(shape, direction, board)
      if not move(shape, 'v', board):
        break
    add_to_board(shape, board)

    first_not_empty_row = next(y for y, row in enumerate(board) if sum(row))
    board = board[first_not_empty_row:]
    height = len(board)
    height_changes.append(height - previous_height)
    previous_height = height
  return height_changes


def find_pattern(lst):
  for start in range(len(lst)):
    for i in range(10, len(lst)//2-start):
      if lst[start:start+i] == lst[start+i:start+2*i]:
        return start, i
  return len(lst), 0

def part2(iterations):
  height_changes = part1(5000)

  start, length = find_pattern(height_changes)
  if start != len(height_changes):
    extra = (iterations-start) % length
    repeats = (iterations-start) // length
    return sum(height_changes[:start + extra]) + sum(height_changes[start:start+length]) * repeats


if __name__ == "__main__":
  t0 = time.time()
  submit(sum(part1(2022)), part="a", day=DAY, year=YEAR)
  submit(part2(int(1e12)), part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)