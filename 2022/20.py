# 20   01:32:04   2456      0   02:30:53   2929      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2022, 20

puzzle = Puzzle(day=DAY, year=YEAR)
indata = [int(x) for x in puzzle.input_data.split('\n')]

class Node:
  def __init__(self, prev, x, nxt):
    self.prev = prev
    self.x = x
    self.nxt = nxt
  
  def move_forward(self, steps):
    for _ in range(steps):
      self.prev.nxt = self.nxt
      self.nxt.prev = self.prev
      self.prev = self.nxt
      self.nxt = self.prev.nxt
      self.prev.nxt = self
      self.nxt.prev = self


def parse_indata(decryption_key):
  numbers = [Node(prev=None, x=indata[0]*decryption_key, nxt=None)]
  for i in range(1, len(indata)):
    num = Node(prev=numbers[-1], x=indata[i]*decryption_key, nxt=None)
    numbers[-1].nxt = num
    numbers.append(num)
  numbers[-1].nxt = numbers[0]
  numbers[0].prev = numbers[-1]
  return numbers


def solve(decryption_key=1, mixing_rounds=1):
  # go through all the numbers and do the mixing
  numbers = parse_indata(decryption_key)
  for _ in range(mixing_rounds):
    for num in numbers:
      steps = num.x%(len(numbers)-1)
      num.move_forward(steps)

  # find zero
  curr = numbers[0]
  while curr.x != 0:
    curr = curr.nxt

  # calculate result
  result = 0
  for _ in range(3):
    for _ in range(1000):
      curr = curr.nxt
    result += curr.x
  return result


if __name__ == "__main__":
  t0 = time.time()
  submit(solve(1, 1), part="a", day=DAY, year=YEAR)
  submit(solve(811589153, 10), part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)
