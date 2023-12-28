# 7   01:08:05   7656      0   09:43:08  28586      0

from aocd.models import Puzzle


def hand_score(hand, part):
    card_dict = {}
    for card in hand:
        if part == "a" or card != "J":
            card_dict[card] = card_dict.get(card, 0) + 1
    count = sorted(card_dict.values()) or [0]
    if part == "b":
        count[-1] += hand.count("J")
    return count[-1] - len(count)


def hand_rank(hand, part):
    score = hand_score(hand, part)
    types = "23456789TJQKA" if part == "a" else "J23456789TQKA"
    return score, *map(types.index, hand)


def solve(indata, part):
    hands = [row.split() for row in indata]
    hands.sort(key=lambda x: hand_rank(x[0], part))
    return sum((i + 1) * int(x[1]) for i, x in enumerate(hands))


if __name__ == "__main__":
    input_data = Puzzle(day=7, year=2023).input_data.split("\n")
    print(f"\npart1: {solve(input_data, 'a')}\npart2: {solve(input_data, 'b')}")
