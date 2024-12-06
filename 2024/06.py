#  6   00:10:35  1278      0   00:22:04   893      0

from aocd.models import Puzzle
import time


def walk(G, start, obstruction=None):
    H, W = len(G), len(G[0])
    y, x = start
    dy, dx = -1, 0
    visited = set()
    is_loop = False

    while True:
        if (y, x, dy, dx) in visited:
            is_loop = True
            break
        visited.add((y, x, dy, dx))

        if not (0 <= y+dy < H and 0 <= x+dx < W):
            break

        if G[y+dy][x+dx] == "#" or (y+dy, x+dx) == obstruction:
            dy, dx = dx, -dy
        else:
            y, x = y+dy, x+dx
    
    return is_loop, visited


def solve(G):
    H, W = len(G), len(G[0])
    start = [(y, x) for y in range(H) for x in range(W) if G[y][x] == '^'][0]

    _, visited_states = walk(G, start)
    visited_positions = {(y, x) for y,x,dy,dx in visited_states}

    part1_answer = len(visited_positions)
    part2_answer = sum(walk(G, start, pos)[0] for pos in visited_positions - {start})

    return part1_answer, part2_answer


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    G = puzzle.input_data.split('\n')

    part1_answer, part2_answer = solve(G)

    print("\npart1:", part1_answer)
    print("\npart2:", part2_answer)
    print("\ntime:", time.time()-t0)