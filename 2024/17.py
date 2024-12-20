# 17   00:25:19  1572      0   02:22:58  1894      0

from aocd.models import Puzzle
import time
import re


def run_program(A, program):
    B = C = i = 0
    res = []
    while i < len(program):
        opcode, literal = program[i:i+2]
        i += 2
        combo = [0, 1, 2, 3, A, B, C, 7][literal]

        match opcode:
            case 0: A = A // 2 ** combo
            case 1: B = B ^ literal
            case 2: B = combo % 8
            case 3: i = literal if A != 0 else i
            case 4: B = B ^ C
            case 5: res += [combo % 8]
            case 6: B = A // 2 ** combo
            case 7: C = A // 2 ** combo

    return res


def part1(A, program):
    res = run_program(A, program)
    return ",".join(map(str, res))


def part2(program):
    ok = {0}
    for num in program[::-1]:
        ok = {8*A + i for A in ok for i in range(8) if run_program(8*A + i, program)[0] == num}
    return min(ok)


if __name__ == "__main__":
    t0 = time.time()
    A, B, C, *program = map(int, re.findall(r'\d+', Puzzle(year=2024, day=17).input_data))
    print("\npart1:", part1(A, program))
    print("\npart2:", part2(program))
    print("\ntime:", time.time()-t0)