# 11   00:09:28  2094      0   00:17:22  1075      0

from aocd.models import Puzzle
import time
from functools import cache


@cache
def update(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return update(1, blinks-1)

    s = str(stone)
    if len(s) % 2 == 0:
        left, right = int(s[:len(s)//2]), int(s[len(s)//2:])
        return update(left, blinks-1) + update(right, blinks-1)
    return update(2024 * stone, blinks-1)


if __name__ == "__main__":
    t0 = time.time()
    stones = [*map(int,Puzzle(2024, 11).input_data.split())]
    print("\npart1:", sum(update(stone, 25) for stone in stones))
    print("\npart2:", sum(update(stone, 75) for stone in stones))
    print("\ntime:", time.time()-t0)