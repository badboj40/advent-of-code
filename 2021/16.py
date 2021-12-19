from copy import deepcopy

with open("input/16", "r") as f:
    indata = f.read()

def hex2bin(hex_string):
    try:
        number, pad, rjust, size, kind = int(hex_string, 16), '0', '>', 4 * len(hex_string), 'b'
        return f'{number:{pad}{rjust}{size}{kind}}'
    except:
        print('hex string', hex_string)


def len_of_packet(bin_input):
    if len(bin_input) < 6:
        return 0
    packet_len = 0
    bin_string = bin_input
    V, T, bin_string = bin_string[:3], bin_string[3:6], bin_string[6:]
    packet_len += 6
    if T == '100':
        value = ''
        while True:
            packet_len += 5
            bit, val, bin_string = bin_string[:1], bin_string[1:5], bin_string[5:]
            value += val
            if bit == '0':
                break
    else:
        I, bin_string = bin_string[:1], bin_string[1:]
        packet_len += 1
        if len(bin_string) > 1:
            if I == '0':
                L, bin_string = bin_string[:15], bin_string[15:]
                packet_len += 15
                L = int(L, 2)
                packet_len += L
            else:
                L, bin_string = bin_string[:11], bin_string[11:]
                L = int(L, 2)
                for i in range(L):
                    res = len_of_packet(bin_string)
                    bin_string = bin_string[res:]
                    packet_len += res
    return packet_len



def parse_packets(bin_input):
    res = 0
    bin_string = bin_input
    i =0

    while bin_string:
        i += 1
        print('i:',i)
        V, T, bin_string = bin_string[:3], bin_string[3:6], bin_string[6:]
        res += int(V, 2)
        if T == '100':
            value = ''
            while True:
                bit, val, bin_string = bin_string[:1], bin_string[1:5], bin_string[5:]
                value += val
                if bit == '0':
                    break
        else:
            I, bin_string = bin_string[:1], bin_string[1:]
            if len(bin_string) > 1:
                if I == '0':
                    L, bin_string = bin_string[:15], bin_string[15:]
                    L = int(L, 2)
                    sub_packets, bin_string = bin_string[:L], bin_string[L:]
                    res += parse_packets(sub_packets)
                else:
                    L, bin_string = bin_string[:11], bin_string[11:]
                    L = int(L, 2)
                    for i in range(L):
                        packet_len = len_of_packet(bin_string)
                        if packet_len == 0:
                            break
                        packet, bin_string = bin_string[:packet_len], bin_string[packet_len:]
                        res += parse_packets(packet)
    return res


def part1():
    bin_string = hex2bin(indata)
    # bin_string = hex2bin('38006F45291200')
    # bin_string = hex2bin('8A004A801A8002F478')
    # bin_string = hex2bin('A0016C880162017C3686B18A3D4780')
    # bin_string = hex2bin('C0015000016115A2E0802F182340')
    # bin_string = hex2bin('620080001611562C8802118E34')
    # bin_string = hex2bin('D2FE28')
    # bin_string = hex2bin('EE00D40C823060')
    return parse_packets(bin_string)
    return len_of_packet(bin_string)


def part2():
    return 0


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
