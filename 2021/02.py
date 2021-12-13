with open("input/02", "r") as f:
    indata = [x.split() for x in f.read().split('\n')]

pos1 = [0, 0] # horizontal, depth
pos2 = [0, 0, 0] # horizontal, depth, aim

for instruction in indata:
    if instruction:
        if instruction[0] == 'forward':
            pos1[0] += int(instruction[1])
            pos2[0] += int(instruction[1])
            pos2[1] += int(instruction[1]) * pos2[2]
        elif instruction[0] == 'down':
            pos1[1] += int(instruction[1])
            pos2[2] += int(instruction[1])
        elif instruction[0] == 'up':
            pos1[1] -= int(instruction[1])
            pos2[2] -= int(instruction[1])

print(f"part1: {pos1[0] * pos1[1]}")
print(f"part2: {pos2[0] * pos2[1]}")
