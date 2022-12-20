import time
import itertools

from aocd.models import Puzzle
YEAR, DAY = 2015, 13
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')

def parse_indata():
  happiness_data = dict()
  for row in indata:
    l = row.split(' ')
    person1 = l[0]
    person2 = l[-1][:-1]
    
    if l[2] == "gain":
      happiness = int(l[3])
    else:
      happiness = -int(l[3])

    if person1 not in happiness_data:
      happiness_data[person1] = dict()
    happiness_data[person1][person2] = happiness

  return happiness_data


def part1(happiness_data):
  best_happiness_change = 0
  persons = happiness_data.keys()

  for perm in itertools.permutations(persons):
    happiness_change = 0
    perm = list(perm) + [perm[0]]
    for i in range(len(perm)-1):
      happiness_change += happiness_data[perm[i]][perm[i+1]]
      happiness_change += happiness_data[perm[i+1]][perm[i]]
      
    best_happiness_change = max(best_happiness_change, happiness_change)
  
  return best_happiness_change


def part2(happiness_data):
  best_happiness_change = 0
  persons = happiness_data.keys()

  for perm in itertools.permutations(persons):
    happiness_change = []
    perm = list(perm) + [perm[0]]
    for i in range(len(perm)-1):
      happiness_change.append(happiness_data[perm[i]][perm[i+1]] + happiness_data[perm[i+1]][perm[i]])

    happiness_change = sum(happiness_change) - min(happiness_change)
    best_happiness_change = max(best_happiness_change, happiness_change)
  
  return best_happiness_change


if __name__ == "__main__":
  t0 = time.time()
  happiness_data = parse_indata()
  print("part1:", part1(happiness_data))
  print("part2:", part2(happiness_data))
  print("time:", time.time()-t0)
