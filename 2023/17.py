# 17   01:18:10   1893      0   02:03:58   2235      0

from aocd.models import Puzzle
import time
import heapq


def move(grid, y, x, dirr, min_step, max_step):
    result = []
    cost = 0
    for step in range(1, max_step + 1):
        y += 1 if dirr == "v" else -1 if dirr == "^" else 0
        x += 1 if dirr == ">" else -1 if dirr == "<" else 0
        if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):
            return result
        cost += grid[y][x]
        if min_step <= step:
            result.append((cost, y, x, dirr))
    return result


def get_neighbors(grid, y, x, dirr, min_step, max_step):
    neighbors = []
    if dirr == "v" or dirr == "^" or dirr == "s":
        neighbors += move(grid, y, x, ">", min_step, max_step)
        neighbors += move(grid, y, x, "<", min_step, max_step)
    if dirr == ">" or dirr == "<" or dirr == "s":
        neighbors += move(grid, y, x, "v", min_step, max_step)
        neighbors += move(grid, y, x, "^", min_step, max_step)
    return neighbors


def dijkstra(grid, min_step, max_step):
    dist = {}
    goal = (len(grid) - 1, len(grid[0]) - 1)
    Q = [(0, 0, 0, "s")]
    while Q:
        cost, y, x, dirr = heapq.heappop(Q)
        if (y, x) == goal:
            return cost
        for ncost, ny, nx, ndirr in get_neighbors(grid, y, x, dirr, min_step, max_step):
            if cost + ncost < dist.get((ny, nx, ndirr), float("inf")):
                dist[(ny, nx, ndirr)] = cost + ncost
                heapq.heappush(Q, (cost + ncost, ny, nx, ndirr))


if __name__ == "__main__":
    t0 = time.time()

    puzzle = Puzzle(day=17, year=2023)
    puzzle_input = puzzle.input_data.split("\n")
    grid = [[int(x) for x in row] for row in puzzle_input]

    part1_answer = dijkstra(grid, min_step=1, max_step=3)
    print("\npart1:", part1_answer)
    part2_answer = dijkstra(grid, min_step=4, max_step=10)
    print("\npart2:", part2_answer)

    print("\ntime:", time.time() - t0)
