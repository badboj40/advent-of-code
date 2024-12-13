# 13   00:13:36  1053      0   01:10:18  3340      0
#
# Did recursive brute force with cache for p1, but for p2 I had to google a real algorithm

from aocd.models import Puzzle
import re
import time


def cramer(a1, a2, b1, b2, c1, c2):
    """
    https://en.wikipedia.org/wiki/Cramer%27s_rule

    for equation system:    a1 * x + b1 * y = c1
                            a2 * x + b2 * y = c2
    
    The solution is:        x = D2/D1    (if D1 != 0)
                            y = D3/D1
    
    for the determinants:    D1 = |a1 b1|, D2 = |c1 b1|, D3 = |a1 c1|
                                  |a2 b2|       |c2 b2|       |a2 c2|
    """
    D1 = a1 * b2 - b1 * a2
    D2 = c1 * b2 - b1 * c2
    D3 = a1 * c2 - c1 * a2

    if D1 == 0: return 0

    x = D2 / D1
    y = D3 / D1

    if x >= 0 and x == int(x) and y >= 0 and y == int(y):
        return 3 * int(x) + int(y)
    return 0


def solve(indata):
    indata = [map(int, re.findall(r'\d+', row)) for row in indata]
    p1 = p2 = 0
    for row in indata:
        ax, ay, bx, by, goalx, goaly = row
        p1 += cramer(ax, ay, bx, by, goalx, goaly)
        p2 += cramer(ax, ay, bx, by, 10000000000000+goalx, 10000000000000+goaly)
    return p1, p2


if __name__ == "__main__":
    t0 = time.time()
    puzzle_input = Puzzle(2024, 13).input_data.split("\n\n")
    p1, p2 = solve(puzzle_input)
    print("\npart1:", p1)
    print("\npart2:", p2)
    print("\ntime:", time.time()-t0)