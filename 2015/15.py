from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time

def parse_input():
  puzzle = Puzzle(year=2015, day=15)
  indata = puzzle.input_data.split('\n')
  ingredients = []
  for row in indata:
    ingredients.append([])
    stats = row.split(':')[1].split(',')
    for stat in stats:
      value = int(stat.strip().split(' ')[1])
      ingredients[-1].append(value)
  return ingredients


def part1(indata):
  ingredients = [x[:-1] for x in indata]
  best_score = 0

  for i in range(101):
    for j in range(101-i):
      for k in range(101-i-j):

        scores = [0] * len(ingredients[0])
        for ii, amount in enumerate([i, j, k, 100-i-j-k]):
          for jj, ingredient in enumerate(ingredients[ii]):
            scores[jj] += amount * ingredient
        scores = [0 if x < 0 else x for x in scores]
        best_score = max(np.prod(scores), best_score)

  return best_score


def part2(indata):
  ingredients = indata
  best_score = 0

  for i in range(101):
    for j in range(101-i):
      for k in range(101-i-j):
        
        scores = [0] * len(ingredients[0])
        for ii, amount in enumerate([i, j, k, 100-i-j-k]):
          for jj, ingredient in enumerate(ingredients[ii]):
            scores[jj] += amount * ingredient
        scores = [0 if x < 0 else x for x in scores]
        if scores[-1] == 500:
          best_score = max(np.prod(scores[:-1]), best_score)

  return best_score


if __name__ == "__main__":
  print() 
  t0 = time.time()
  indata = parse_input()

  part1_answer = part1(indata)

  print("part1:", part1_answer)
  submit(part1_answer, part="a", day=15, year=2015)

  part2_answer = part2(indata)
  print("part2:", part2_answer)
  submit(part2_answer, part="b", day=15, year=2015)

  print("time:", time.time()-t0)
