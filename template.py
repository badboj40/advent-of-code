from aocd.models import Puzzle
from aocd import submit
import numpy as np
import re
import time


def part1(indata):
    return


def part2(indata):
    return


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n")
    example_input = puzzle.examples[0].input_data.split("\n")

    ex1 = part1(example_input)
    ex1_answer = int(puzzle.examples[0].answer_a)
    assert ex1 == ex1_answer, f"Ex1: expected {ex1_answer}, got {ex1}"

    part1_answer = part1(puzzle_input)
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    ex2 = part2(example_input)
    ex2_answer = int(puzzle.examples[0].answer_b)
    assert ex2 == ex2_answer, f"Ex2: expected {ex2_answer}, got {ex2}"

    part2_answer = part2(puzzle_input)
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)
        
    print("\ntime:", time.time()-t0)