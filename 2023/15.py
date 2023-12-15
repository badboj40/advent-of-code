# 15   00:04:44   1090      0   00:39:05   3247      0

from aocd.models import Puzzle
import re


def hash_alg(word):
    res = 0
    for c in word:
        res += ord(c)
        res *= 17
        res %= 256
    return res


def part1(indata):
    return sum(hash_alg(word) for word in indata)


def part2(indata):
    boxes = [[] for _ in range(256)]

    for word in indata:
        label = re.match(r"\w+", word)[0]
        i = hash_alg(label)
        j = next((j for j, b in enumerate(boxes[i]) if b[0] == label), -1)
        num = int(word.split("=")[1]) if "=" in word else 0

        if j >= 0 and "=" in word:
            boxes[i][j][1] = num
        elif j >= 0 and "-" in word:
            boxes[i] = boxes[i][:j] + boxes[i][j + 1 :]
        elif "=" in word:
            boxes[i].append([label, num])

    res = 0
    for i, box in enumerate(boxes):
        res += (i + 1) * sum((j + 1) * b[1] for j, b in enumerate(box))
    return res


if __name__ == "__main__":
    puzzle = Puzzle(day=15, year=2023)
    puzzle_input = puzzle.input_data.split(",")
    print(f"\npart1: {part1(puzzle_input)}\npart2: {part2(puzzle_input)}")
