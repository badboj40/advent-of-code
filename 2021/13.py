from copy import deepcopy
import statistics

class Paper:
    def __init__(self, coords):
        x_max = max(coords, key=lambda item: item[0])[0]
        y_max = max(coords, key=lambda item: item[1])[1]
        paper = [['.'] * (x_max + 1) for row in range(y_max + 1)]
        for x, y in coords:
            paper[y][x] = '#'
        self.paper = paper

    def count_hashtags(self):
        hashtags = 0
        for row in self.paper:
            hashtags += row.count('#')
        return hashtags

    def show(self, axis='', fold_index=0):
        for row in self.paper:
            print(''.join(row))

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


if __name__ == "__main__":
    with open("input/13", "r") as f:
        indata = f.read().split('\n\n')
    coords = [[int(e) for e in coord.split(',')] for coord in indata[0].split('\n')]
    folds = indata[1].split('\n')[:-1]

    paper = Paper(coords)
    for i, fold in enumerate(folds):
        axis, fold_index = fold.split()[2].split('=')
        fold_index = int(fold_index)
        paper.fold(axis, fold_index)
        if i == 0:
            print("part1:", paper.count_hashtags())
    print("part2:")
    paper.show()
