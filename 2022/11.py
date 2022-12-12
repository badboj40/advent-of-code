# 11   11:40:16  34044      0   11:46:47  25556      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR = int('2022')
DAY = int('11')

puzzle = Puzzle(day=DAY, year=YEAR)
indata = [data.split('\n') for data in puzzle.input_data.split('\n\n')]

class Monkey:
  def __init__(self, id, starting_items, operation, test, divisibility):
    self.id = id
    self.items = starting_items
    self.operation = operation
    self.test = test
    self.inspected_items = 0
    self.divisibility = divisibility


def parse_input():
  monkeys = []
  for id, monkey_data in enumerate(indata):
    starting_items = [int(x) for x in monkey_data[1].split(': ')[1].split(',')]
    operation_data = monkey_data[2].split('old ')[1].split(' ')
    test_data = []
    for i in range(3, 6):
      test_data.append(int(monkey_data[i].split(' ')[-1]))

    # using a function factory to avoid late-binding errors. More info here:
    # https://stackoverflow.com/a/3431699
    def make_functions(factor, test_data):
      if factor == 'old':
        def operation(x): return x * x
      elif operation_data[0] == '*':
        def operation(x): return x * int(factor)
      else:
        def operation(x): return x + int(factor)
      def test(x): return test_data[1] if x % test_data[0] == 0 else test_data[2]
      return operation, test
    
    operation, test = make_functions(operation_data[1], test_data)
    monkeys.append(Monkey(id, starting_items, operation, test, test_data[0]))

  return monkeys


def part1():
  monkeys = parse_input()
  for _ in range(20):
    for monkey in monkeys:
      while monkey.items:
        new_worry_level = monkey.operation(monkey.items.pop(0)) // 3
        target_monkey = monkey.test(new_worry_level)
        monkeys[target_monkey].items.append(new_worry_level)
        monkey.inspected_items += 1

  inspection_count = sorted([monkey.inspected_items for monkey in monkeys])
  return inspection_count[-1] * inspection_count[-2]


def part2():
  monkeys = parse_input()
  divisibility = 1
  for monkey in monkeys:
    divisibility *= monkey.divisibility

  for _ in range(10000):
    for monkey in monkeys:
      while monkey.items:
        # The worry level does not need to be larger than the product of 
        # every monkey's divisibility number that is used for decision making.
        new_worry_level = monkey.operation(monkey.items.pop(0)) % divisibility
        target_monkey = monkey.test(new_worry_level)
        monkeys[target_monkey].items.append(new_worry_level)
        monkey.inspected_items += 1

  inspection_count = sorted([monkey.inspected_items for monkey in monkeys])
  return inspection_count[-1] * inspection_count[-2]


if __name__ == "__main__":
  t0 = time.time()

  part1_answer = part1()
  print("\npart1:", part1_answer)
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2()
  print("\npart2:", part2_answer)
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)
