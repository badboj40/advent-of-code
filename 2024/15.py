# 15   00:28:21  1950      0   02:33:41  3883      0

from aocd.models import Puzzle
import time, copy


def swap(G, y, x, ny, nx):
    G[ny][nx], G[y][x] = G[y][x], G[ny][nx]


def move(G, y, x, dy, dx, already_copied=False):
    if G[y][x] in ".#":
        return G[y][x] == "."
    ny, nx = y + dy, x + dx

    # Moving a large box vertically
    if G[y][x] in "[]" and dy:
        offsets = (0, 1) if G[y][x] == "[" else (-1, 0)
        G_copy = copy.deepcopy(G) if not already_copied else G
        if all(move(G_copy, ny, nx+offset, dy, dx, True) for offset in offsets):
            G[:] = G_copy
            for offset in offsets:
                swap(G, y, x + offset, ny, nx + offset)
            return True
    # All other cases
    elif move(G, ny, nx, dy, dx):
        swap(G, y, x, ny, nx)
        return True

    return False


def solve(G, moves):
    y, x = [(y, x) for y in range(len(G)) for x in range(len(G[0])) if G[y][x] == "@"][0]
    for dy, dx in moves:
        if move(G, y, x, dy, dx):
            y, x = y + dy, x + dx
    return sum(100 * y + x for y in range(len(G)) for x in range(len(G[0])) if G[y][x] in "O[")


if __name__ == "__main__":
    t0 = time.time()
    indata = Puzzle(2024, 15).input_data.split("\n\n")
    D = {"#": "##", "O": "[]", "." : "..", "@": "@."}
    G1 = [*map(list, indata[0].split("\n"))]
    G2 = [list("".join([D[c] for c in row])) for row in G1]
    moves = [{"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}[d] for d in indata[1].replace("\n", "")]

    print("\npart1:", solve(G1, moves))
    print("\npart2:", solve(G2, moves))
    print("\ntime:", time.time()-t0)