import time
import itertools

from aocd.models import Puzzle
YEAR, DAY = 2015, 9
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')


def parse_input():
  cities = []
  for row in indata:
    a = row.split(' ')[0]
    b = row.split(' ')[2]
    if a not in cities:
      cities.append(a)
    if b not in cities:
      cities.append(b)

  graph = [[0 for x in range(len(cities))] for y in range(len(cities))]
  for row in indata:
    a, _, b, _, distance = row.split(' ')
    graph[cities.index(a)][cities.index(b)] = int(distance)
    graph[cities.index(b)][cities.index(a)] = int(distance)
  
  return graph


def part1(graph):
  mincost = float('inf')
  cities = [i for i in range(len(graph))]

  for permutation in itertools.permutations(cities):
    pathcost = 0
    for i in range(len(permutation)-1):
      j = permutation[i]
      k = permutation[i+1]
      pathcost += graph[j][k]
    mincost = min(mincost, pathcost)
  
  return mincost


def part2(graph):
  maxcost = float(0)
  cities = [i for i in range(len(graph))]

  for permutation in itertools.permutations(cities):
    pathcost = 0
    for i in range(len(permutation)-1):
      j = permutation[i]
      k = permutation[i+1]
      pathcost += graph[j][k]
    maxcost = max(maxcost, pathcost)
  
  return maxcost


if __name__ == "__main__":
  t0 = time.time()
  graph = parse_input()
  print("part1:", part1(graph))
  print("part2:", part2(graph))

  print("time:", time.time()-t0)
