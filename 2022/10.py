# 10   00:45:48   8597      0   01:00:02   6371      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR = int('2022')
DAY = int('10')

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')


def part1():
  X = 1
  score = 0
  cpu_queue = []
  for i in range(220):
    # start of execution
    if i < len(indata):
      cpu_queue += [0] if indata[i]=='noop' else [0, int(indata[i].split(' ')[1])]
    
    # during the execution
    if i+1 in [20, 60, 100, 140, 180, 220]:
      score += (i+1) * X

    # end of execution
    X += cpu_queue.pop(0)

  return score


def print_letter(i, X):
  if i % 40 in [X-1, X, X+1]:
    print('#',end='')
  else:
    print('.',end='')
  if i % 40 == 39:
    print()


def part2():
  X = 1
  cpu_queue = []
  for i in range(240):
    # start of execution
    if i < len(indata):
      cpu_queue += [0] if indata[i]=='noop' else [0, int(indata[i].split(' ')[1])]

    # during the execution
    print_letter(i, X)

    # end of execution
    X += cpu_queue.pop(0)


if __name__ == "__main__":
  t0 = time.time()

  part1_answer = part1()
  print("\npart1:", part1_answer)
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  print('\npart2:\n')
  part2()

  print("\ntime:", time.time()-t0)
