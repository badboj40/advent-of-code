#  4   00:27:05  5598      0   00:34:21  4109      0

from aocd.models import Puzzle
import time


def part1(y, x, G, H, W):
    s = 0
    for dy, dx in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        if not (0 <= y + 3*dy < H and 0 <= x + 3*dx < W):
            continue
        s += 'XMAS' == ''.join([G[y + i*dy][x + i*dx] for i in range(4)])
    return s


def part2(y, x, G, H, W):
    if G[y][x] != "A" or not (1 <= y < H-1 and 1 <= x < W-1):
        return 0
    diag1 = G[y-1][x-1] + G[y+1][x+1] 
    diag2 = G[y+1][x-1] + G[y-1][x+1] 
    return set(diag1) == set(diag2) == set("SM")


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    G = puzzle.input_data.split("\n")
    H, W = len(G), len(G[0])

    part1_answer = sum(part1(y, x, G, H, W) for y in range(H) for x in range(W))
    print("\npart1:", part1_answer)

    part2_answer = sum(part2(y, x, G, H, W) for y in range(H) for x in range(W))
    print("\npart2:", part2_answer)
        
    print("\ntime:", time.time()-t0)