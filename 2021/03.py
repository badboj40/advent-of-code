with open("input/03", "r") as f:
    indata = f.read().split('\n')

ones = [0] * len(indata[0])

for binary in indata:
    for i, digit in enumerate(binary):
        if digit == '1':
            ones[i] += 1

gamma = ""
epsilon = ""

for x in ones:
    if x > len(indata) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(f"part1: {gamma * epsilon}")

oxygen_list = indata.copy()
i = 0
while len(oxygen_list) > 1:
    ones = 0
    for binary in oxygen_list:
        if binary and binary[i] == '1':
            ones += 1
    if ones >= len(oxygen_list) / 2:
        most_frequent = '1'
    else:
        most_frequent = '0'
    oxygen_list = [x for x in oxygen_list if x and x[i] == most_frequent]
    i += 1

oxygen = int(oxygen_list[0], 2)

co2_list = indata.copy()
i = 0
while len(co2_list) > 1:
    ones = 0
    for binary in co2_list:
        if binary and binary[i] == '1':
            ones += 1
    if ones < len(co2_list) / 2:
        least_frequent = '1'
    else:
        least_frequent = '0'
    co2_list = [x for x in co2_list if x and x[i] == least_frequent]
    i += 1

co2 = int(co2_list[0], 2)

print(f"part2: {oxygen * co2}")


