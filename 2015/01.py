# Solution took 00:04:52

def part1(indata):
    res = 0
    for c in indata:
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
    return res


def part2(indata):
    res = 0
    for i, c in enumerate(indata):
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
        if res < 0:
            return i+1


if __name__ == "__main__":
    with open("input/01", "r") as f:
        indata = f.read()


    print("part1:", part1(indata))
    print("part2:", part2(indata))
