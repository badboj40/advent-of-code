# Solution took 00:16:15

import hashlib

def part1(indata):
    i = 0
    while True:
        i += 1
        string = indata + str(i)
        if hashlib.md5(string.encode('UTF-8')).hexdigest()[:5] == '00000':
            return i


def part2(indata):
    i = 0
    while True:
        i += 1
        string = indata + str(i)
        if hashlib.md5(string.encode('UTF-8')).hexdigest()[:6] == '000000':
            return i


if __name__ == "__main__":
    with open("input/04", "r") as f:
        indata = f.read().strip()

    print("part1:", part1(indata))
    print("part2:", part2(indata))
