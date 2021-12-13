from copy import deepcopy
import statistics

with open("input/13", "r") as f:
    indata = f.read().split('\n')

class Paper:
    def __init__(self):
        x_max = 0
        y_max = 0
        for line in indata:
            if line and 'fold' not in line:
                x, y = [int(d) for d in line.split(',')]
                if x > x_max:
                    x_max = x
                if y > y_max:
                    y_max = y
        paper = [['.'] * (x_max + 1) for row in range(y_max + 1)]
        for line in indata:
            if line and 'fold' not in line:
                x, y = [int(d) for d in line.split(',')]
                paper[y][x] = '#'
        self.paper = paper

    def count_hashtags(self):
        hashtags = 0
        for row in self.paper:
            hashtags += row.count('#')
        return hashtags

    def show(self, axis='', fold_index=0):
        if axis == 'y':
            for i, row in enumerate(self.paper):
                if i != int(fold_index):
                    print(''.join(row))
                else:
                    print('-' * len(row))
        elif axis == 'x':
            for row in self.paper:
                print(''.join(row)[:fold_index] + '|' + ''.join(row)[fold_index+1:])
        else:
            for row in self.paper:
                print(''.join(row))
        print()

    def fold(self, axis, fold_index):
        width = len(self.paper[0]) if axis == 'y' else fold_index
        height = fold_index if axis == 'y' else len(self.paper)
        folded_paper = [['.'] * width for row in range(height)]

        if axis == 'y':
            y_max = min(fold_index, len(self.paper)-fold_index-1)
            for y in range(1, y_max + 1):
                for x in range(width):
                    folded_paper[height-y][x] = '#' if (self.paper[height-y][x] == '#' or self.paper[height+y][x] == '#') else '.'
        elif axis == 'x':
            x_max = min(fold_index, len(self.paper[0])-fold_index-1)
            for y in range(height):
                for x in range(1, x_max + 1):
                    folded_paper[y][width-x] = '#' if (self.paper[y][width-x] == '#' or self.paper[y][width+x] == '#') else '.'
        self.paper = folded_paper


def part1():
    paper = Paper()
    for line in indata:
        if 'fold' in line:
            axis, fold_index = line.split()[2].split('=')
            fold_index = int(fold_index)
            print("hashtags innan fold:", paper.count_hashtags())
            #paper.show(axis, fold_index)
            paper.fold(axis, fold_index)
            #paper.show()
            break
    return paper.count_hashtags()


def part2():
    paper = Paper()
    for line in indata:
        if 'fold' in line:
            axis, fold_index = line.split()[2].split('=')
            fold_index = int(fold_index)
            paper.fold(axis, fold_index)
    paper.show()


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:")
    part2()
