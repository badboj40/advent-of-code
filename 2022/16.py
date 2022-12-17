# 16   02:11:54   2070      0       >24h  10689      0

from aocd.models import Puzzle
import re
import time

YEAR = int("2022")
DAY = int("16")

puzzle = Puzzle(day=DAY, year=YEAR)
indata = [re.findall(r"[A-Z]{2}|\d+", row) for row in puzzle.input_data.split("\n")]

valve_map = {row[0]: row[2:] for row in indata}
locked_valves = {row[0]: int(row[1]) for row in indata if int(row[1]) != 0}
total_pressure = sum(int(row[1]) for row in indata)


def find_shortest_paths(root):
    queue = [root]
    paths = {root: [root]}
    while queue:
        node = queue.pop(0)
        for child in valve_map[node]:
            if child not in paths:
                paths[child] = paths[node] + [child]
                queue.append(child)
    return paths

paths = {(root, goal): find_shortest_paths(root)[goal] for root in valve_map for goal in valve_map}


def move(roots, locked_valves, time_left, goals):
  released_pressure = total_pressure - sum(locked_valves.values())

  # If the time ran out or there are no more valves to be unlocked
  if time_left <= 1 or not locked_valves:
    return released_pressure * time_left
  
  # If there are still unassigned goals, assign new ones
  if None in goals and any(valve not in goals for valve in locked_valves):
    index = goals.index(None)
    possible_goals = []
    for valve in sorted([valve for valve in locked_valves if valve not in goals], reverse=True):
      new_goals = goals.copy()
      new_goals[index] = valve
      possible_goals.append(new_goals)
    number_of_elements = max(5, len(locked_valves)-3)
    return max(move(roots, locked_valves, time_left, goals) for goals in possible_goals[:number_of_elements])

  # If any goal is reached, turn off the valve and remove the goal
  if any(root == goal for root in roots for goal in goals):
    locked_valves = locked_valves.copy()
    for root, goal in zip(roots, goals):
      if root == goal:
        locked_valves.pop(goal)
    goals = [goal if root != goal else None for root, goal in zip(roots, goals)]
  
  # for all roots that have goals, move them towards their goal
  if None not in goals:
    closest_goal = min(len(paths[(root, goal)]) for root, goal in zip(roots, goals) if goal) - 1
  else:
    closest_goal = 1
  roots = [paths[(root, goal)][closest_goal] if goal else root for root, goal in zip(roots, goals)]
  return closest_goal * released_pressure + move(roots, locked_valves, time_left-closest_goal, goals)



t0 = time.time()
print("part1:", move(['AA'], locked_valves, 30, [None]))

# very slow solution for part 2, takes almost 8 minutes
print("part2: minutes:26" , move(['AA', 'AA'], locked_valves, 26, [None, None]))
print(f"\n{time.time()-t0}")
