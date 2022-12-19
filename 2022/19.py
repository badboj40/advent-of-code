# 19   04:12:05   2453      0   17:40:44   6653      0

from aocd.models import Puzzle
from aocd import submit
import re
import time

YEAR, DAY = 2022, 19

puzzle = Puzzle(day=DAY, year=YEAR)
indata = [tuple(int(d) for d in re.findall(r"\d+", row)) for row in puzzle.input_data.split("\n")]
most_geodes = 0


def solve(state, bp, visited):
  global most_geodes
  t, ore, clay, obsidian, geodes, r1, r2, r3 = state

  # if time is up, the state is already visited or if the 
  if t == 0 or state in visited or geodes + t*(t-1)//2 < most_geodes:
    return geodes
  visited.add(state)

  new_states = []
  # geode robot (adding the amount of geodes it would mine in the time it has left)
  if ore >= bp[5] and obsidian >= bp[6]:
    new_states.append((t-1, ore+r1-bp[5], clay+r2, obsidian+r3-bp[6], geodes+(t-1), r1, r2, r3))
  # obsidian robot (r3)
  if ore >= bp[3] and clay >= bp[4]:
    new_states.append((t-1, ore+r1-bp[3], clay+r2-bp[4], obsidian+r3, geodes, r1, r2, r3+1))
  # clay robot (r2)
  if ore >= bp[2]:
    new_states.append((t-1, ore+r1-bp[2], clay+r2, obsidian+r3, geodes, r1, r2+1, r3))
  # ore robot (r1)
  if ore >= bp[1]:
    new_states.append((t-1, ore+r1-bp[1], clay+r2, obsidian+r3, geodes, r1+1, r2, r3))
  # no robot
  if ore < max((bp[1], bp[2], bp[3], bp[5])):
    new_states.append((t-1, ore+r1, clay+r2, obsidian+r3, geodes, r1, r2, r3))

  most_geodes = max(most_geodes, max(solve(new_state, bp, visited) for new_state in new_states))
  return most_geodes


def part1():
  global most_geodes
  score = 0
  for blueprint in indata:
    most_geodes = 0
    geodes = solve((24, 0, 0, 0, 0, 1, 0, 0), blueprint, set())
    score += geodes * blueprint[0]
  return score


def part2():
  global most_geodes
  score = 1
  for blueprint in indata[:3]:
    most_geodes = 0
    geodes = solve((32, 0, 0, 0, 0, 1, 0, 0), blueprint, set())
    score *= geodes
  return score


if __name__ == "__main__":
  t0 = time.time()
  submit(part1(), part="a", day=DAY, year=YEAR)
  submit(part2(), part="b", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)