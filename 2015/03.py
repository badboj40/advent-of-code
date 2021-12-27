# Solution took 00:07:37

def part1(indata):
    recieved = {(0, 0)}
    pos = (0, 0)
    for char in indata:
        if char == '^':
            pos = (pos[0], pos[1]+1)
        elif char == 'v':
            pos = (pos[0], pos[1]-1)
        elif char == '>':
            pos = (pos[0]+1, pos[1])
        elif char == '<':
            pos = (pos[0]-1, pos[1])
        recieved.add(pos)
    return len(recieved)


def part2(indata):
    recieved = {(0, 0)}
    p1 = (0, 0)
    p2 = (0, 0)
    for i, char in enumerate(indata):
        if i % 2 == 0:
            if char == '^':
                p1 = (p1[0], p1[1]+1)
            elif char == 'v':
                p1 = (p1[0], p1[1]-1)
            elif char == '>':
                p1 = (p1[0]+1, p1[1])
            elif char == '<':
                p1 = (p1[0]-1, p1[1])
            recieved.add(p1)
        else:
            if char == '^':
                p2 = (p2[0], p2[1]+1)
            elif char == 'v':
                p2 = (p2[0], p2[1]-1)
            elif char == '>':
                p2 = (p2[0]+1, p2[1])
            elif char == '<':
                p2 = (p2[0]-1, p2[1])
            recieved.add(p2)

    return len(recieved)


if __name__ == "__main__":
    with open("input/03", "r") as f:
        indata = f.read()

    print("part1:", part1(indata))
    print("part2:", part2(indata))
