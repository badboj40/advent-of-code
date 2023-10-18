from aocd.models import Puzzle
from aocd import submit
import re
import time

YEAR, DAY = 2015, 19
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n\n')


def part1():
    rules = [rule.split(' => ') for rule in indata[0].split('\n')]
    molecule = indata[1]
    new_molecules = set()
    for rule in rules:
        indexes = [m.start() for m in re.finditer(f'(?={rule[0]})', molecule)]
        for i in indexes:
            new_molecules.add(molecule[:i] + rule[1] + molecule[i+len(rule[0]):])
    return len(new_molecules)


def find_first_match(molecule, rules):
    for i in range(len(molecule)):
        for rule in rules:
            if molecule[i:].startswith(rule[0]):
                return rule


def part2():
    """
    Start from the end of the molecule and apply the inverse of the first rule
    that matches. Repeat until the molecule is 'e'.
    """
    rules = [rule[::-1].split(' >= ') for rule in indata[0].split('\n')]
    molecule = indata[1][::-1]
    steps = 0
    while molecule != 'e':
        rule = find_first_match(molecule, rules)
        molecule = molecule.replace(rule[0], rule[1], 1)
        steps += 1
    return steps


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
