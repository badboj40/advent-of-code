# Solution took 00:27:23

def is_nice_string1(string):
    vowels = 0
    has_double = False
    contain_bad = False
    for i in range(len(string)):
        if i >= 1 and string[i] == string[i-1]:
            has_double = True
        if string[i] in 'aeiou':
            vowels += 1
    for bad in ['ab', 'cd', 'pq', 'xy']:
        if bad in string:
            contain_bad = True
    return has_double and vowels >= 3 and not contain_bad


def part1(indata):
    nice_strings = 0
    for string in indata:
        if is_nice_string1(string):
            nice_strings += 1
    return nice_strings


def is_nice_string2(string):
    has_repeating = False
    has_double_pair = False
    for i in range(2, len(string)):
        first_part, pair, second_part = string[:i-2], string[i-2:i], string[i:]
        if pair in first_part or pair in second_part:
            has_double_pair = True
        if string[i] == string[i-2]:
            has_repeating = True
    return has_repeating and has_double_pair


def part2(indata):
    nice_strings = 0
    for string in indata:
        if is_nice_string2(string):
            nice_strings += 1
    return nice_strings


if __name__ == "__main__":
    with open("input/05", "r") as f:
        indata = f.read().split('\n')

    print("part1:", part1(indata))
    print("part2:", part2(indata))
