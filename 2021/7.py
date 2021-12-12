with open("input/7", "r") as f:
    indata = [int(x) for x in f.read().split(',')]

def part1():
    cheapest = float('Inf')
    for pos in range(max(indata)+1):
        cost = 0
        for x in indata:
            cost += abs(x-pos)
        if cost < cheapest:
            cheapest = cost
    return cheapest

def part2():
    cheapest = float('Inf')
    for pos in range(max(indata)+1):
        cost = 0
        for x in indata:
            cost += abs(x-pos) * (abs(x-pos) + 1) / 2
        if cost < cheapest:
            cheapest = cost
    return int(cheapest)

print("part1:", part1())
print("part2:", part2())

