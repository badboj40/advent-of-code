# 23   00:23:46    849      0   01:22:45    851      0

# Slow again, runs in ~13 seconds with pypy3

from aocd.models import Puzzle


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


def dfs(graph, start, goal):
    stack = [(start, {start}, 0)]
    longest_path = 0

    while stack:
        pos, path, path_length = stack.pop()

        if pos == goal:
            longest_path = max(longest_path, path_length)
            continue

        for neighbor, dist in graph[pos].items():
            if neighbor not in path:
                stack.append((neighbor, path | {neighbor}, path_length + dist))

    return longest_path


def solve(indata, part):
    graph = make_graph(indata, part)
    if part == "b":
        contract(graph)
    goal = (len(indata) - 1, indata[-1].index("."))
    return dfs(graph, (0, 1), goal)


if __name__ == "__main__":
    input_data = Puzzle(day=23, year=2023).input_data.split("\n")
    print(f"\npart1: {solve(input_data, 'a')}\npart2: {solve(input_data, 'b')}")
