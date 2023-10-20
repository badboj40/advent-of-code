from aocd.models import Puzzle
from aocd import submit
import time

directory, filename = __file__.split('/')[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')


def split_row(row):
    outside = []
    inside = []
    current = ''
    for char in row:
        if char == '[':
            outside.append(current)
            current = ''
        elif char == ']':
            inside.append(current)
            current = ''
        else:
            current += char
    outside.append(current)
    return outside, inside


def is_abba(word):
    for i in range(len(word)-3):
        if word[i] == word[i+3] and word[i+1] == word[i+2] and word[i] != word[i+1]:
            return True
    return False


def get_abas(wordlist):
    abas = set()
    for word in wordlist:
        for i in range(len(word)-2):
            if word[i] == word[i+2] and word[i] != word[i+1]:
                abas.add(word[i:i+3])
    return abas


def part1():
    count = 0
    for row in indata:
        outside, inside = split_row(row)
        if any(is_abba(w) for w in outside) and not any(is_abba(w) for w in inside):
            count += 1
    return count


def part2():
    count = 0
    for row in indata:
        outside, inside = split_row(row)
        for aba in get_abas(outside):
            bab = aba[1] + aba[0] + aba[1]
            if any(bab in w for w in inside):
                count += 1
                break
    return count


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = part1()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = part2()
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
