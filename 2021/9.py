from copy import deepcopy
with open("input/9", "r") as f:
    indata = [[int(x) for x in row] for row in f.read().split('\n')][:-1]

map_height = len(indata)
map_width = len(indata[0])

def part1():
    risk_sum = 0
    for y in range(map_height):
        for x in range(map_width):
            point = indata[y][x]
            up = indata[y-1][x] if y >= 1 else float("Inf")
            down = indata[y+1][x] if y < map_height-1 else float("Inf")
            left = indata[y][x-1] if x >= 1 else float("Inf")
            right = indata[y][x+1] if x < map_width-1 else float("Inf")
            if point < up and point < down and point < left and point < right:
                risk_sum += point+1
    return risk_sum



def part2():
    data = deepcopy(indata)

    def explore(y, x):
        if y < 0 or y >= map_height or x < 0 or x >= map_width or data[y][x] == 9:
            return 0
        data[y][x] = 9
        return 1 + explore(y-1, x) + explore(y+1, x) + explore(y, x-1) + explore(y, x+1)

    basins = []
    for y in range(map_height):
        for x in range(map_width):
            res = explore(y, x)
            if res > 0:
                basins.append(res)
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]

if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
