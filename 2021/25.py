from copy import deepcopy


class Seafloor:
    def __init__(self, data):
        self.seafloor = data

    def move(self):
        moved = False
        new_seafloor = deepcopy(self.seafloor)
        height = len(self.seafloor)
        width = len(self.seafloor[0])
        for y in range(height):
            for x in range(width):
                if self.seafloor[y][x] == '>' and self.seafloor[y][(x+1)%width] == '.':
                    moved = True
                    new_seafloor[y][x] = '.'
                    new_seafloor[y][(x+1)%width] = '>'
        self.seafloor = deepcopy(new_seafloor)
        for y in range(height):
            for x in range(width):
                if self.seafloor[y][x] == 'v' and self.seafloor[(y+1)%height][x] == '.':
                    moved = True
                    new_seafloor[y][x] = '.'
                    new_seafloor[(y+1)%height][x] = 'v'
        self.seafloor = deepcopy(new_seafloor)
        return moved

    def __str__(self):
        string = ''
        for row in self.seafloor:
            string += ''.join(row) + '\n'
        return string


def part1(indata):
    seafloor = Seafloor(indata)
    i = 1
    while seafloor.move():
        i += 1
    return i


def part2():
    return 0


if __name__ == "__main__":
    with open("input/25", "r") as f:
        indata = [[char for char in line] for line in f.read().split('\n')[:-1]]

    print("part1:", part1(indata))
    print("part2:", part2())
