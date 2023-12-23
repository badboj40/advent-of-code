# 23   00:23:46    849      0   01:22:45    851      0

# Slow again, runs in ~22 seconds with pypy3

from aocd.models import Puzzle
import time

import sys

sys.setrecursionlimit(10000)


def get_neighbors(grid, y, x, part):
    directions = {"<": (y, x - 1), ">": (y, x + 1), "^": (y - 1, x), "v": (y + 1, x)}

    if part == "a" and grid[y][x] in directions:
        return {directions[grid[y][x]]: 1}

    return {
        (ny, nx): 1
        for ny, nx in directions.values()
        if 0 <= ny < len(grid) and grid[ny][nx] != "#"
    }


def make_graph(indata, part):
    return {
        (y, x): get_neighbors(indata, y, x, part)
        for y, row in enumerate(indata)
        for x, tile in enumerate(row)
        if tile != "#"
    }


def contract(graph):
    nodes = list(graph.keys())
    for pos in nodes:
        if len(graph.get(pos, [])) == 2:
            pos1, pos2 = graph.pop(pos)
            dist = graph[pos1].pop(pos) + graph[pos2].pop(pos)
            graph[pos1][pos2] = dist
            graph[pos2][pos1] = dist


def dfs(graph, pos, goal, visited, length):
    if pos == goal:
        return length
    paths = [0]
    for neighbor in graph[pos]:
        if neighbor not in visited:
            dist = graph[pos][neighbor]
            paths += [dfs(graph, neighbor, goal, visited | {pos}, length + dist)]
    return max(paths)


def solve(indata, part):
    graph = make_graph(indata, part)
    if part == "b":
        contract(graph)
    goal = (len(indata) - 1, indata[-1].index("."))
    return dfs(graph, (0, 1), goal, set(), 0)


if __name__ == "__main__":
    t0 = time.time()
    input_data = Puzzle(day=23, year=2023).input_data.split("\n")
    print(f"\npart1: {solve(input_data, 'a')}\npart2: {solve(input_data, 'b')}")
    print("\ntime:", time.time() - t0)
