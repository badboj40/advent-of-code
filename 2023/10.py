# 10       >24h  46575      0       >24h  37203      0

from aocd.models import Puzzle
from aocd import submit
import numpy as np
import re
import time

from matplotlib.path import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from collections import deque


def parse(indata):
    graph = {}
    start = None
    for y, row in enumerate(indata):
        for x, char in enumerate(row):
            match char:
                case "|":
                    graph[(y, x)] = [(y - 1, x), (y + 1, x)]
                case "-":
                    graph[(y, x)] = [(y, x - 1), (y, x + 1)]
                case "L":
                    graph[(y, x)] = [(y - 1, x), (y, x + 1)]
                case "J":
                    graph[(y, x)] = [(y - 1, x), (y, x - 1)]
                case "7":
                    graph[(y, x)] = [(y + 1, x), (y, x - 1)]
                case "F":
                    graph[(y, x)] = [(y + 1, x), (y, x + 1)]
                case "S":
                    graph[(y, x)] = [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]
                    start = (y, x)
                case ".":
                    pass
    return graph, start


def dfs(graph, start):
    loop = []
    stack = [start]
    visited = set()
    while stack:
        cur = stack.pop()
        loop.append(cur)
        visited.add(cur)
        for neighbor in graph.get(cur, []):
            if cur in graph.get(neighbor, []) and neighbor not in visited:
                stack.append(neighbor)

    return loop


def part1(indata):
    graph, start = parse(indata)
    loop = dfs(graph, start)

    return len(loop) // 2


def part2(indata, debug=False):
    graph, start = parse(indata)
    loop = dfs(graph, start)
    path = Path(loop)

    fig, ax = plt.subplots()
    patch = patches.PathPatch(path, facecolor="gray", lw=1)
    ax.add_patch(patch)
    ax.set_xlim(-1, len(indata))
    ax.set_ylim(-1, len(indata[0]))
    plt.show()

    res = 0
    for y in range(len(indata)):
        row = ""
        for x in range(len(indata[0])):
            if (y, x) not in dist:
                if path.contains_point((y, x)):
                    res += 1

    return res


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split("/")[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n")

    part1_answer = part1(puzzle_input)
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2(puzzle_input)
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
