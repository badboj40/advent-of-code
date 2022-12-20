# Solution took 00:23:11


from aocd.models import Puzzle
YEAR, DAY = 2015, 6
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')[:-1]

def part1():
    grid = [[0] * 1000 for x in range(1000)]
    for row in indata:
        data = row.split()
        if data[0] == 'toggle':
            state = 'toggle'
        else:
            state = data[1]
        x0, y0 = [int(e) for e in data[-3].split(',')]
        x1, y1 = [int(e) for e in data[-1].split(',')]
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                if state == 'on' or state == 'toggle' and grid[y][x] == 0:
                    grid[y][x] = 1
                elif state == 'off' or state == 'toggle' and grid[y][x] == 1:
                    grid[y][x] = 0
    lit = 0
    for row in grid:
        lit += sum(row)
    return lit


def part2():
    grid = [[0] * 1000 for x in range(1000)]
    for row in indata:
        data = row.split()
        if data[0] == 'toggle':
            state = 'toggle'
        else:
            state = data[1]
        x0, y0 = [int(e) for e in data[-3].split(',')]
        x1, y1 = [int(e) for e in data[-1].split(',')]
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                if state == 'on':
                    grid[y][x] += 1
                elif state == 'off' and grid[y][x] > 0:
                    grid[y][x] -= 1
                elif state == 'toggle':
                    grid[y][x] += 2
    lit = 0
    for row in grid:
        lit += sum(row)
    return lit


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
