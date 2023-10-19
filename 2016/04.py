from aocd.models import Puzzle
from aocd import submit
import re
import time

YEAR, DAY = 2016, 4

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')


def part1():
    result = 0
    for room in indata:
        code, number, checksum = re.match(r"([a-z-]+)-(\d+)\[(\w+)\]", room).groups()
        chars = {c: code.count(c) for c in set(code) if c != '-'}
        chars = sorted(chars.items(), key=lambda x: (-x[1], x[0]))
        if "".join([c for c,_ in chars[:5]]) == checksum:
            result += int(number)
    return result


def part2():
    result = 0
    for room in indata:
        code, number, checksum = re.match(r"([a-z-]+)-(\d+)\[(\w+)\]", room).groups()
        new_code = ""
        for c in code:
            if c == '-':
                new_code += ' '
            else:
                new_code += chr((ord(c)-ord('a')+int(number))%26 + ord('a'))
        if "object" in new_code:
            return number
    return


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
