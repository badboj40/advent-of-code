# 15   00:28:21  1950      0   02:33:41  3883      0

from aocd.models import Puzzle
import time
import copy


def score(G):
    return sum(100 * y + x for y in range(len(G)) for x in range(len(G[0])) if G[y][x] in "O[")


def swap(G, y, x, ny, nx):
    G[ny][nx], G[y][x] = G[y][x], G[ny][nx]


def move(G, y, x, d, copied=False):
    if G[y][x] in ".#":
        return G[y][x] == "."

    dy, dx = {"^" : (-1,0), ">" : (0,1), "v" : (1,0), "<" : (0,-1)}[d]
    ny, nx = y + dy, x + dx

    if G[y][x] in "[]" and d in "v^":
        left_offset  = 1 if G[y][x] == "]" else 0
        right_offset = 1 if G[y][x] == "[" else 0
        G_copy = copy.deepcopy(G) if not copied else G
        if move(G_copy, ny, nx-left_offset, d, True) and move(G_copy, ny, nx+right_offset, d, True):
            G[:] = G_copy
            swap(G, y, x - left_offset, ny, nx - left_offset)
            swap(G, y, x + right_offset, ny, nx + right_offset)
            return True
        else:
            return False

    if move(G, ny, nx, d):
        swap(G, y, x, ny, nx)
        return True

    return False


def solve(indata):
    moves = "".join(indata[1].split("\n"))

    D = {"#": "##", "O": "[]", "." : "..", "@": "@."}
    G1 = [[c for c in row] for row in indata[0].split("\n")]
    G2 = [[c for c in "".join([D[c] for c in row])] for row in indata[0].split("\n")]

    y1, x1 = [(y, x) for y in range(len(G1)) for x in range(len(G1[0])) if G1[y][x] == "@"][0]
    y2, x2 = [(y, x) for y in range(len(G2)) for x in range(len(G2[0])) if G2[y][x] == "@"][0]

    for d in moves:
        dy, dx = {"^" : (-1,0), ">" : (0,1), "v" : (1,0), "<" : (0,-1)}[d]
        if move(G1, y1, x1, d):
            y1, x1 = y1 + dy, x1 + dx
        if move(G2, y2, x2, d):
            y2, x2 = y2 + dy, x2 + dx

    return score(G1), score(G2)


if __name__ == "__main__":
    t0 = time.time()
    indata = Puzzle(2024, 15).input_data.split("\n\n")
    p1, p2 = solve(indata)
    print("\npart1:", p1)
    print("\npart2:", p2)
    print("\ntime:", time.time()-t0)