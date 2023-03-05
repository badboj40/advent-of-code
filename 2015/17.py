from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2015, 17

puzzle = Puzzle(day=DAY, year=YEAR)
containers = [int(x) for x in puzzle.input_data.split('\n')]

containers_used = {}


def solve(containers, liters, goal, used):
    if liters == goal:
        containers_used[used] = containers_used.get(used, 0) + 1
        return 1
    if liters > goal or not containers:
        return 0
    
    container, *containers = containers
    return solve(containers, liters+container, goal, used+1) + solve(containers, liters, goal, used)


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = solve(containers, 0, 150, 0)
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = containers_used[min(containers_used)]
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
