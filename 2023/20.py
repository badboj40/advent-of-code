# 20   01:18:01   2308      0   02:15:03   1787      0

from aocd.models import Puzzle
from aocd import submit
import time
import math

from collections import deque


def parse(indata):
    modules = {}
    for row in indata:
        src, dest = row.split(" -> ")
        dest = dest.split(", ")
        if src == "broadcaster":
            modules[src] = ("", dest, 0)
        else:
            op, src = src[0], src[1:]
            modules[src] = (op, dest, 0)

    all_parents = {}
    for module, (op, dest, prev) in modules.items():
        parents = {}
        for module2, (op2, dest2, prev2) in modules.items():
            if module in dest2:
                parents[module2] = 0
        all_parents[module] = parents

    for module, (op, dest, prev) in modules.items():
        parents = all_parents[module]
        modules[module] = [op, dest, prev, parents]

    return modules


def press_button(modules, part="a", goal_nodes=[]):
    Q = deque([("button", "broadcaster", 0)])
    found = None
    signals = []
    while Q:
        sender, module, signal = Q.popleft()
        if part == "b" and signal == 0 and module in goal_nodes:
            found = module

        signals.append(signal)

        if module not in modules:
            continue

        op, dest, prev, parents = modules[module]
    
        if op == "%" and signal == 1:
            continue

        new_signal = signal
        if op == "%":
            new_signal = (prev + 1) % 2
            modules[module][2] = new_signal
        elif op == "&":
            parents[sender] = signal
            new_signal = 1 if 0 in parents.values() else 0
            modules[module][2] = new_signal

        Q.extend([(module, d, new_signal) for d in dest])

    if part == "b":
        return found

    return signals.count(0), signals.count(1)


def part1(indata):
    modules = parse(indata)
    low, high = zip(*[press_button(modules) for _ in range(1000)])
    return sum(low) * sum(high)


def part2(indata):
    modules = parse(indata)

    for module, (op, dest, prev, parents) in modules.items():
        if "rx" in dest:
            rx_parent = module
            break
    goal_nodes = [module for module in modules[rx_parent][3]]

    result = 1
    i = 0
    while goal_nodes:
        i += 1
        found = press_button(modules, part="b", goal_nodes=goal_nodes)
        if found in goal_nodes:
            goal_nodes.remove(found)
            result *= i

    return result


if __name__ == "__main__":
    puzzle = Puzzle(day=20, year=2023)
    puzzle_input = puzzle.input_data.split("\n")
    p1 = part1(puzzle_input)
    p2 = part2(puzzle_input)
    assert p1 == 739960225 and p2 == 231897990075517
    print(f"\npart1: {part1(puzzle_input)}\npart2: {part2(puzzle_input)}")
