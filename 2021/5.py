import re

with open("input/5", "r") as f:
    indata = f.read().split('\n')


terrain1 = [[0] * 1000 for x in range(1000)]
terrain2 = [[0] * 1000 for x in range(1000)]
for row in indata:
    if re.findall(r'\d+', row):
        x1, y1, x2, y2 = [int(x) for x in re.findall(r'\d+', row)]
        if x1 == x2: #vertical
            for y in range(min(y1,y2), max(y1,y2)+1):
                terrain1[y][x1] += 1
                terrain2[y][x1] += 1
        elif y1 == y2: #horizontal
            for x in range(min(x1,x2), max(x1,x2)+1):
                terrain1[y1][x] += 1
                terrain2[y1][x] += 1
        else: #diagonal
            x_coords = [x for x in range(min(x1, x2), max(x1,x2)+1)]
            if x1 > x2:
                x_coords = x_coords[::-1]
            y_coords = [y for y in range(min(y1, y2), max(y1,y2)+1)]
            if y1 > y2:
                y_coords = y_coords[::-1]
            for i in range(len(x_coords)):
                x = x_coords[i]
                y = y_coords[i]
                terrain2[y][x] += 1


def count_dangerous(terrain):
    dangerous_tiles = 0
    for row in terrain:
        for tile in row:
            if tile >= 2:
                dangerous_tiles += 1
    return dangerous_tiles


print(f"part1: {count_dangerous(terrain1)}")
print(f"part2: {count_dangerous(terrain2)}")
