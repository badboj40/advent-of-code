# 7   01:08:05   7656      0   09:43:08  28586      0

from aocd.models import Puzzle
from aocd import submit
import numpy as np
import re
import time

import itertools

def count_hand(hand):
    card_dict = {}
    for card in hand:
        card_dict[card] = card_dict.get(card, 0) + 1
    return sorted(card_dict.values())


def hand_rank(hand):
    count = count_hand(hand)
    return (
        7 * (count == [5])
        + 6 * (count == [1, 4])
        + 5 * (count == [2, 3])
        + 4 * (count == [1, 1, 3])
        + 3 * (count == [1, 2, 2])
        + 2 * (count == [1, 1, 1, 2])
        + 1 * (count == [1, 1, 1, 1, 1])
    )

class Hand:
    def __init__(self, hand_input, part, joker_hand=None):
        cards, bid = hand_input.split()
        self.bid = int(bid)
        self.cards = cards
        self.part = part
        self.joker_hand = joker_hand

        if part == "a":
            self.types = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        else:
            self.types = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
            if joker_hand is None:
                self.set_joker_hand()

    def set_joker_hand(self):
        jokers = self.cards.count("J")

        if jokers > 0:
            joker_combinations = [''.join(x) for x in itertools.combinations_with_replacement(self.types[1:], jokers)]
            regular_cards = "".join([card for card in self.cards if card != "J"])
            joker_hands = [f"{regular_cards + x}" for x in joker_combinations]
            jh = [Hand(f"{self.cards} 0", "b", x) for x in joker_hands]
            jh.sort()
            joker_hands = [x.joker_hand for x in jh]
            self.joker_hand = joker_hands[-1]
    
    def __lt__(self, other):
        rank_self = hand_rank(self.joker_hand or self.cards) 
        rank_other = hand_rank(other.joker_hand or other.cards)
        if rank_self != rank_other:
            return rank_self < rank_other

        for c1, c2 in zip(self.cards, other.cards):
            if c1 != c2:
                return self.types.index(c1) < self.types.index(c2)

        return False
    

def solve(indata, part):
    hands = [Hand(row, part=part) for row in indata]
    hands.sort()
    return sum((i + 1) * hand.bid for i, hand in enumerate(hands))


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split("/")[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n")

    part1_answer = solve(puzzle_input, 'a')
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = solve(puzzle_input, 'b')
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
