#  12   00:19:49  2041      0   02:35:55  5274      0

from aocd.models import Puzzle
import time


def get_regions(G):
    visited = set()
    H, W = len(G), len(G[0])

    def dfs(y, x, region_type):
        if (y, x) in visited or not (0 <= y < H and 0 <= x < W) or G[y][x] != region_type:
            return []
        visited.add((y, x))
        return [(y, x)] + sum([dfs(y+dy, x+dx, region_type) for dy,dx in [(-1,0), (0,1), (1,0), (0,-1)]], [])

    return [dfs(y, x, G[y][x]) for y in range(H) for x in range(W) if (y, x) not in visited]


def get_perimeter(region):
    vertical = [] # (y, x)
    horizontal = [] # (x, y) - invererted axis
    for (y, x) in region:
        if (y-1,x) not in region: horizontal.append((y-0.1, x)) # above
        if (y+1,x) not in region: horizontal.append((y+0.1, x)) # below
        if (y,x-1) not in region:   vertical.append((x-0.1, y)) # left
        if (y,x+1) not in region:   vertical.append((x+0.1, y)) # right
    return sorted(horizontal) + sorted(vertical)
    

def discounted_length(perimeter):
    count = 0
    prev = (None, None)
    for fence in perimeter:
        if prev[0] != fence[0] or prev[1] + 1 != fence[1]:
            count += 1
        prev = fence
    return count


def solve(indata):
    G = [[c for c in row] for row in indata]
    regions = get_regions(G)
    p1 = p2 = 0
    for region in regions:
        perimeter = get_perimeter(region)
        p1 += len(region) * len(perimeter)
        p2 += len(region) * discounted_length(perimeter)
    return p1, p2


if __name__ == "__main__":
    t0 = time.time()
    puzzle_input = Puzzle(2024, 12).input_data.split("\n")
    p1, p2 = solve(puzzle_input)
    print("\npart1:", p1)
    print("\npart2:", p2)
    assert p1 == 1450816 and p2 == 865662
    print("\ntime:", time.time()-t0)