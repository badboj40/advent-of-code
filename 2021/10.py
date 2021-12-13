from copy import deepcopy
import statistics

with open("input/10", "r") as f:
    indata = f.read().split()

match = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
error_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
autocomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def get_error_score(indata):
    def find_end(char, line):
        while line and isinstance(line, str):
            if line[0] == match[char]:
                return line[1:]
            elif line[0] in ')]}>':
                return error_points[line[0]]
            else:
                line = find_end(line[0], line[1:])
        if not line:
            return 0
        return line

    res = find_end(indata[0], indata[1:])
    while isinstance(res, str):
        res = find_end(res[0], res[1:])
    return res


def get_autocomplete_score(indata):
    def find_end(char, line):
        while line and isinstance(line, str):
            if line[0] == match[char]:
                return line[1:]
            else:
                line = find_end(line[0], line[1:])
                if isinstance(line, list):
                    return line + [match[char]]
        if not line:
            return [match[char]]

    res = find_end(indata[0], indata[1:])
    while isinstance(res, str):
        res = find_end(res[0], res[1:])

    autocomplete_score = 0
    for char in res:
        autocomplete_score = 5 * autocomplete_score + autocomplete_points[char]
    return autocomplete_score


def part1():
    data = deepcopy(indata)
    error_score = 0
    for row in data:
        error_score += get_error_score(row)
    return error_score

def part2():
    data = deepcopy(indata)
    autocomplete_scores = []
    for row in data:
        if get_error_score(row) == 0:
            autocomplete_scores.append(get_autocomplete_score(row))
    autocomplete_scores.sort()
    return statistics.median(autocomplete_scores)

if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())

