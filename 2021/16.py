from copy import deepcopy
import math


def hex2bin(hex_string):
    res = ''
    for char in hex_string:
        res += f'{int(char, 16):04b}'
    return res


def part1(bin_string):
    result = 0
    V, T, bin_string = int(bin_string[:3], 2), int(bin_string[3:6], 2), bin_string[6:]
    result += V
    if T == 4:
        while bin_string[0] != '0':
            bin_string = bin_string[5:]
        bin_string = bin_string[5:]
    else:
        I, bin_string = bin_string[:1], bin_string[1:]
        if I == '0':
            L, bin_string = int(bin_string[:15], 2), bin_string[15:]
            sub_packets, bin_string = bin_string[:L], bin_string[L:]
            while sub_packets:
                sub_packets, res = part1(sub_packets)
                result += res
        else:
            L, bin_string = int(bin_string[:11], 2), bin_string[11:]
            for i in range(L):
                bin_string, res = part1(bin_string)
                result += res
    return bin_string, result


def calc_res(results, T):
    if T == 0:
        return sum(results)
    elif T == 1:
        return math.prod(results)
    elif T == 2:
        return min(results)
    elif T == 3:
        return max(results)
    elif T == 4:
        return results[0]
    elif T == 5:
        return int(results[0] > results[1])
    elif T == 6:
        return int(results[0] < results[1])
    elif T == 7:
        return int(results[0] == results[1])


def part2(bin_string):
    results = []
    V, T, bin_string = int(bin_string[:3], 2), int(bin_string[3:6], 2), bin_string[6:]
    if T == 4:
        res = ''
        while bin_string:
            bit, val, bin_string = bin_string[:1], bin_string[1:5], bin_string[5:]
            res += val
            if bit == '0':
                break
        results.append(int(res, 2))
    else:
        I, bin_string = bin_string[:1], bin_string[1:]
        if I == '0':
            L, bin_string = int(bin_string[:15], 2), bin_string[15:]
            sub_packets, bin_string = bin_string[:L], bin_string[L:]
            while sub_packets:
                sub_packets, res = part2(sub_packets)
                results.append(res)
        else:
            L, bin_string = int(bin_string[:11], 2), bin_string[11:]
            for i in range(L):
                bin_string, res = part2(bin_string)
                results.append(res)
    return bin_string, calc_res(results, T)


if __name__ == "__main__":
    with open("input/16", "r") as f:
        indata = f.read()[:-1]
    bin_string = hex2bin(indata)

    print("part1:", part1(bin_string)[1])
    print("part2:", part2(bin_string)[1])
