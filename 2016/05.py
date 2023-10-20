from aocd.models import Puzzle
from aocd import submit
import numpy as np
import time
import hashlib

YEAR, DAY = 2016, 5

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data


def part1():
    password = ""
    i = 0
    while len(password) < 8:
        md5 = hashlib.md5((indata+str(i)).encode()).hexdigest()
        if md5.startswith("00000"):
            password += md5[5]
        i += 1 
    return password


def part2():
    password = ['-']*8
    i = 0
    while '-' in password:
        md5 = hashlib.md5((indata+str(i)).encode()).hexdigest()
        if md5.startswith("00000") and md5[5] < '8' and password[int(md5[5])] == '-':
            password[int(md5[5])] = md5[6]
        i += 1 
    return ''.join(password)


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
