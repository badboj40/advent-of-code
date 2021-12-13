from copy import deepcopy

with open("input/11", "r") as f:
    indata = [[int(x) for x in row] for row in f.read().split()]

class Octopus():
    def __init__(self):
        self.grid = deepcopy(indata)
        self.has_flashed = []

    def flash(self, y, x):
        if self.has_flashed[y][x]:
            return 0
        self.grid[y][x] += 1
        if self.grid[y][x] <= 9:
            return 0
        else:
            self.has_flashed[y][x] = 1
            self.grid[y][x] = 0
            flashes = 1
            for i in range(y-1, y+2):
                for j in range(x-1, x+2):
                    if 0 <= i < 10 and 0 <= j < 10 and (i, j) != (y, x):
                        flashes += self.flash(i, j)
            return flashes

    def step(self):
        self.has_flashed = [[0] * 10 for x in range(10)]
        flashes = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                flashes += self.flash(i, j)
        return flashes

    def show(self):
        for row in self.grid:
            print(' '.join([str(x) for x in row]))
        print()


def part1():
    octopus = Octopus()
    flashes = 0
    for i in range(100):
        flashes += octopus.step()
    return flashes


def part2():
    octopus = Octopus()
    i = 1
    while octopus.step() < 100:
        i += 1
    return i


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
