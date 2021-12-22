import math, json
from copy import deepcopy

class Number:
    def __init__(self, data=0, depth=0):
        self.depth = depth
        if isinstance(data, int):
            self.x = None
            self.y = None
            self.val = data
        else:
            self.x = Number(data[0], depth+1)
            self.y = Number(data[1], depth+1)
            self.val = None

    def is_leaf(self):
        return self.x is None and self.y is None

    def is_pair(self):
        return not self.is_leaf() and self.x.is_leaf() and self.y.is_leaf()

    def get_leaves(self):
        leaves = []
        if self.is_leaf():
            leaves.append(self)
        else:
            leaves.extend(self.x.get_leaves())
            leaves.extend(self.y.get_leaves())
        return leaves

    def get_pairs(self):
        if self.is_leaf():
            return []
        elif self.is_pair():
            return [self]
        else:
            return self.x.get_pairs() + self.y.get_pairs()

    def add(n1_in, n2_in):
        n1 = deepcopy(n1_in)
        n2 = deepcopy(n2_in)
        root = Number()
        n1.increase_depth()
        n2.increase_depth()
        root.x = n1
        root.y = n2
        while root.explode() or root.split():
            pass # Not done
        return root

    def increase_depth(self):
        self.depth += 1
        if self.x is not None:
            self.x.increase_depth()
        if self.y is not None:
            self.y.increase_depth()

    def explode(self):
        pairs = self.get_pairs()
        leaves = self.get_leaves()
        for pair in pairs:
            if pair.depth == 4:
                i = leaves.index(pair.x)
                if i > 0:
                    leaves[i-1].val += pair.x.val
                if i+2 < len(leaves):
                    leaves[i+2].val += pair.y.val
                pair.x = None
                pair.y = None
                pair.val = 0
                return True
        return False

    def split(self):
        leaves = self.get_leaves()
        for leaf in leaves:
            if leaf.val >= 10:
                leaf.x = Number(math.floor(leaf.val/2), leaf.depth+1)
                leaf.y = Number(math.ceil(leaf.val/2), leaf.depth+1)
                return True
        return False

    def magnitude(self):
        if self.is_leaf():
            return self.val
        else:
            return 3 * self.x.magnitude() + 2 * self.y.magnitude()

    def __str__(self):
        if self.is_leaf():
            return str(self.val)
        else:
            return f"[{str(self.x)},{str(self.y)}]"


def part1(indata):
    root = Number(indata[0])
    for row in indata[1:]:
        num = Number(row)
        root = Number.add(root, Number(row))
    return root.magnitude()


def part2(indata):
    max_magnitude = 0
    numbers = [Number(row) for row in indata]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                num = Number.add(numbers[i], numbers[j])
                max_magnitude = max(max_magnitude, num.magnitude())
    return max_magnitude


if __name__ == "__main__":
    with open("input/18", "r") as f:
        indata = [json.loads(x) for x in f.read().split('\n')[:-1]]

    print("part1:", part1(indata))
    print("part2:", part2(indata))
