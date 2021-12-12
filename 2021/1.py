with open("input/1", "r") as f:
    indata = [int(x) for x in f.read().split()]


previous = indata[0]
increases = 0
for depth in indata:
    if depth > previous:
        increases += 1
    previous = depth

print(f"part1: {increases}")


previous = indata[0] + indata[1] + indata[2]
increases = 0
for i in range(len(indata) - 2):
    if indata[i] + indata[i+1] + indata[i+2] > previous:
        increases += 1
    previous = depth
    previous = indata[i] + indata[i+1] + indata[i+2]

print(f"part2: {increases}")
