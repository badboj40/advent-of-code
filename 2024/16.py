# 16   00:20:47  1349      0   00:51:07  1449      0

from aocd.models import Puzzle
import time
import heapq


def best_seats(goals, prevs):
    on_path = set()
    for goal in goals:
        seats = {goal}
        while seats:
            cur = seats.pop()
            if not cur:
                continue
            on_path.add((cur[0], cur[1]))
            seats |= prevs[cur]
    return len(on_path)


def explore(G, start):
    Q = [(0, (*start, 0, 1), None)]
    visited = {}
    prevs = {}
    goals = set()
    best = float("inf")

    while Q:
        score, cur, prev = heapq.heappop(Q)
        y, x, dy, dx = cur
        if G[y][x] == "#" or score > min(best, visited.get(cur, float("inf"))):
            continue

        prevs[cur] = prevs.get(cur, set()) | {prev}
        visited[cur] = score

        if G[y][x] == "E":
            goals.add(cur)
            best = min(best, score)
            continue
        heapq.heappush(Q, (score + 1000, (y, x, dx, -dy), cur)) # rotate counter clockwise
        heapq.heappush(Q, (score + 1000, (y, x, -dx, dy), cur)) # rotate clockwise
        heapq.heappush(Q, (score + 1, (y+dy, x+dx, dy, dx), cur)) # move forward

    return best, best_seats(goals, prevs)


if __name__ == "__main__":
    t0 = time.time()
    G = Puzzle(2024, 16).input_data.split("\n")
    start = [(y, x) for y in range(len(G)) for x in range(len(G[0])) if G[y][x] == "S"][0]
    p1, p2 = explore(G, start)
    print(f"\npart1: {p1}\npart2: {p2}\n\ntime: {time.time()-t0}")