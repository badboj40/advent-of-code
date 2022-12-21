# 21   00:19:17   2005      0   01:08:12   2094      0

from aocd.models import Puzzle
from aocd import submit
import time
from sympy.solvers import solve

YEAR, DAY = 2022, 21

puzzle = Puzzle(day=DAY, year=YEAR)
indata = [row.split(':') for row in puzzle.input_data.split('\n')]
monkeys = {row[0]: row[1].strip().split(' ') for row in indata}


def dfs(part, monkey='root'):
  if part == 2 and monkey=='humn':
    return 'humn'
  if len(monkeys[monkey]) == 1:
    return monkeys[monkey][0]

  left = dfs(part, monkeys[monkey][0])
  op = monkeys[monkey][1]
  right = dfs(part, monkeys[monkey][2])

  if part == 1 and monkey == 'root':
    return f"Eq(({left}{op}{right}),x)"
  if part == 2 and monkey == 'root':
    return f"Eq({left},{right})"
  return f"({left}{op}{right})"


if __name__ == "__main__":
  t0 = time.time()
  part1 = solve(dfs(part=1), 'x')[0]
  part2 = solve(dfs(part=2), 'humn')[0]

  submit(part1, part="a", day=DAY, year=YEAR)
  submit(part2, part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)