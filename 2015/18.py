from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time

YEAR, DAY = 2015, 18

puzzle = Puzzle(day=DAY, year=YEAR)

H = W = 100


neighbors = [
    (-1,-1), (-1,0), (-1,1),
    (0, -1),         (0, 1),
    (1, -1), (1, 0), (1, 1),   
]

def next_state(graph, part2=False):
    new_graph = []

    for y in range(H):
        row = []
        for x in range(W):
            n = sum(0<=y+dy<100 and 0<=x+dx<100 and graph[y+dy][x+dx]=='#' for dy,dx in neighbors)
            if part2 and (y, x) in [(0, 0), (0, W-1), (H-1, 0), (H-1, W-1)]:
                row.append('#')
            elif graph[y][x] == '#' and 2 <= n <= 3 or graph[y][x] == '.' and n==3:
                row.append('#')
            else:
                row.append('.')
        new_graph.append(row)
    return new_graph


def part1():
    graph = puzzle.input_data.split('\n')
    for _ in range(100):
        graph = next_state(graph)
    
    return sum(row.count('#') for row in graph)


def part2():
    graph = puzzle.input_data.split('\n')
    for _ in range(100):
        graph = next_state(graph, part2=True)
    return sum(row.count('#') for row in graph)


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
