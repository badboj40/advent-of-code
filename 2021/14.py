from copy import deepcopy

with open("input/14", "r") as f:
    indata = f.read().split('\n')[:-1]


def step1(poly, instr):
    pairs = []
    for i in range(len(poly)-1):
        pairs.append(poly[i] + poly[i+1])
    res = pairs[0][0] + instr[pairs[0]] + pairs[0][1]
    for pair in pairs[1:]:
        res += instr[pair] + pair[1]
    return res


def part1(poly, instr):
    for i in range(10):
        poly = step1(poly, instr)

    occurances = dict()
    for char in set(poly):
        occurances[char] = poly.count(char)

    return max(occurances.values()) - min(occurances.values())


def step2(pairs, occurances, instr):
    new_pairs = dict()
    new_occurances = deepcopy(occurances)
    for pair in pairs.keys():
        new1 = pair[0] + instr[pair]
        new2 = instr[pair] + pair[1]
        char = instr[pair]
        if new1 not in new_pairs:
            new_pairs[new1] = 0
        if new2 not in new_pairs:
            new_pairs[new2] = 0
        if char not in new_occurances:
            new_occurances[char] = 0
        new_pairs[new1] += pairs[pair]
        new_pairs[new2] += pairs[pair]
        new_occurances[char] += pairs[pair]
    return new_pairs, new_occurances


def part2(poly, instr):
    pairs = dict()
    for i in range(len(poly)-1):
        pair = poly[i] + poly[i+1]
        if pair not in pairs:
            pairs[pair] = 0
        pairs[pair] += 1

    occurances = dict()
    for char in set(poly):
        occurances[char] = poly.count(char)

    for i in range(40):
        pairs, occurances = step2(pairs, occurances, instr)

    return max(occurances.values()) - min(occurances.values())


if __name__ == "__main__":
    poly = indata[0]
    instructions = dict()
    instr_list = [x.split(' -> ') for x in indata[2:]]
    for i in range(len(instr_list)):
        instructions[instr_list[i][0]] = instr_list[i][1]

    print("part1:", part1(poly, instructions))
    print("part2:", part2(poly, instructions))
