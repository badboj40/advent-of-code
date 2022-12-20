# 20   01:32:04   2456      0   02:30:53   2929      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2022, 20

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')
indata = [int(x) for x in puzzle.input_data.split('\n')]


class Node:
  def __init__(self, prev, x, nxt):
    self.prev = prev
    self.x = x
    self.nxt = nxt
  
  def __str__(self):
    return str(self.x)


def part1():
  first = Node(None, indata[0], None)
  numbers = [first]
  for i in range(1, len(indata)):
    num = Node(numbers[-1], indata[i], None)
    numbers[-1].nxt = num
    numbers.append(num)
  numbers[-1].nxt = numbers[0]
  numbers[0].prev = numbers[-1]

  curr = first
  row = ""
  for _ in range(len(numbers)):
    row += f"{str(curr.x):>2} "
    curr = curr.nxt
  print(f"\n{0:>2}:\t{row}")

  
  for num in numbers:
    steps = num.x%(len(numbers)-1)
    for _ in range(steps):
      prev = num.prev
      nxt = num.nxt
      prev.nxt = nxt
      nxt.prev = prev
      num.prev = nxt
      num.nxt = nxt.nxt
      nxt.nxt.prev = num
      nxt.nxt = num

    # curr = num
    # row = ""
    # for _ in range(len(numbers)):
    #   row += f"{str(curr.x):>2} "
    #   curr = curr.nxt
    # print(f"\n{num.x:>2},{steps}:\t{row}")
  
  curr = first
  while curr.x != 0:
    curr = curr.nxt

  cumsum = 0

  for i in range(3):
    for i in range(1000):
      curr = curr.nxt
    print(f"num {1}: {curr.x}")
    cumsum += curr.x


  return cumsum



def part2():
  DECRYPTION_KEY = 811589153
  
  first = Node(None, indata[0]*DECRYPTION_KEY, None)
  numbers = [first]
  for i in range(1, len(indata)):
    num = Node(numbers[-1], indata[i]*DECRYPTION_KEY, None)
    numbers[-1].nxt = num
    numbers.append(num)
  numbers[-1].nxt = numbers[0]
  numbers[0].prev = numbers[-1]

  # curr = first
  # row = ""
  # for _ in range(len(numbers)):
  #   row += f"{str(curr.x//DECRYPTION_KEY):>2} "
  #   curr = curr.nxt
  # print(f"\nstrt:\t{row}")

  
  for _ in range(10):
    for num in numbers:
      steps = num.x%(len(numbers)-1)
      for _ in range(steps):
        prev = num.prev
        nxt = num.nxt
        prev.nxt = nxt
        nxt.prev = prev
        num.prev = nxt
        num.nxt = nxt.nxt
        nxt.nxt.prev = num
        nxt.nxt = num


  curr = first
  while curr.x != 0:
    curr = curr.nxt
  
  # row = ""
  # for _ in range(len(numbers)):
  #   row += f"{str(curr.x//DECRYPTION_KEY):>2} "
  #   curr = curr.nxt
  # print(f"\n{num.x//DECRYPTION_KEY:>2}:\t{row}")

  cumsum = 0

  for i in range(3):
    for i in range(1000):
      curr = curr.nxt
    print(f"num {1}: {curr.x}")
    cumsum += curr.x


  return cumsum


if __name__ == "__main__":
  t0 = time.time()

  part1_answer = part1()
  print("\npart1:", part1_answer)
  # submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2()
  print("\npart2:", part2_answer)
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)
