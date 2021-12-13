with open("input/08", "r") as f:
    indata = f.read().split('\n')

def part1():
    output_values = []
    for row in indata:
        output_values.extend(row.split()[-4:])

    easy_digits = 0
    for val in output_values:
        if len(val) == 2 or len(val) == 3 or len(val) == 4 or len(val) == 7:
            easy_digits += 1
    return easy_digits


def number_from_signal(signal, mapping):
    sevenseg_code = "".join(sorted([mapping[segment] for segment in signal]))
    sevenseg_mapping = {
            'abcefg' : '0',
            'cf'     : '1',
            'acdeg'  : '2',
            'acdfg'  : '3',
            'bcdf'   : '4',
            'abdfg'  : '5',
            'abdefg' : '6',
            'acf'    : '7',
            'abcdefg': '8',
            'abcdfg' : '9'
        }
    return sevenseg_mapping[sevenseg_code]


def part2():
    tot_sum = 0
    for row in indata:
        if row:
            output = row.split()[-4:]
            signals = row.split()[:-5]

            one   = [signal for signal in signals if len(signal) == 2][0]
            seven = [signal for signal in signals if len(signal) == 3][0]
            four  = [signal for signal in signals if len(signal) == 4][0]

            mapping = dict()
            segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            zero_to_nine_string = ''.join(signals)
            for segment in segments:
                count = zero_to_nine_string.count(segment)
                # Because we know that our signals are representing one of each digit
                # we know how many of each segment we should expect. To solve the
                # ambiguity of 7 and 8 occurances we use the fact that the digits one,
                # seven and four are uniquely distinguishable because of their length.
                if count == 4:
                    mapping[segment] = 'e'
                elif count == 6:
                    mapping[segment] = 'b'
                elif count == 7 and segment in four:
                    mapping[segment] = 'd'
                elif count == 7:
                    mapping[segment] = 'g'
                elif count == 8 and segment in seven and segment not in one:
                    mapping[segment] = 'a'
                elif count == 8:
                    mapping[segment] = 'c'
                elif count == 9:
                    mapping[segment] = 'f'
            val = ""
            for signal in output:
                val += number_from_signal(signal, mapping)
            tot_sum += int(val)
    return tot_sum


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
