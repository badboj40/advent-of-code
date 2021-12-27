# Solution took 00:09:59

def part1(indata):
    res = 0
    for row in indata:
        l, w, h = sorted([int(x) for x in row.split('x')])
        res += 3 * l * w + 2 * w * h + 2 * h * l
    return res


def part2(indata):
    res = 0
    for row in indata:
        l, w, h = sorted([int(x) for x in row.split('x')])
        res += 2 * l + 2 * w + l * w * h
    return res


if __name__ == "__main__":
    with open("input/02", "r") as f:
        indata = f.read().split('\n')[:-1]

    print("part1:", part1(indata))
    print("part2:", part2(indata))
