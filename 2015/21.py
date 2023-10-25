from aocd.models import Puzzle
from aocd import submit
import re
import time

directory, filename = __file__.split("/")[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data

BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR = map(int, re.findall(r"\d+", indata))
PLAYER_HP = 100

"""
Brute force solution, but very few combinations to check.
"""

#    name: [cost, damage, armor]
weapons = {
    "Dagger": [8, 4, 0],
    "Shortsword": [10, 5, 0],
    "Warhammer": [25, 6, 0],
    "Longsword": [40, 7, 0],
    "Greataxe": [74, 8, 0],
}

armors = {
    "Leather": [13, 0, 1],
    "Chainmail": [31, 0, 2],
    "Splintmail": [53, 0, 3],
    "Bandedmail": [75, 0, 4],
    "Platemail": [102, 0, 5],
    "None": [0, 0, 0],
}

rings = {
    "Damage +1": [25, 1, 0],
    "Damage +2": [50, 2, 0],
    "Damage +3": [100, 3, 0],
    "Defense +1": [20, 0, 1],
    "Defense +2": [40, 0, 2],
    "Defense +3": [80, 0, 3],
    "None": [0, 0, 0],
}

all_combinations = [
    (w, a, r1, r2)
    for w in weapons
    for a in armors
    for r1 in rings
    for r2 in rings
    if r1 != r2 or r1 == "None"
]


def get_cost(w, a, r1, r2):
    return weapons[w][0] + armors[a][0] + rings[r1][0] + rings[r2][0]


def get_damage(w, a, r1, r2):
    return weapons[w][1] + armors[a][1] + rings[r1][1] + rings[r2][1]


def get_armor(w, a, r1, r2):
    return weapons[w][2] + armors[a][2] + rings[r1][2] + rings[r2][2]


def fight(player_damage, player_armor):
    player_hp = PLAYER_HP
    boss_hp, boss_damage, boss_armor = BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR
    while True:
        boss_hp -= max(1, player_damage - boss_armor)
        if boss_hp <= 0:
            return True
        player_hp -= max(1, boss_damage - player_armor)
        if player_hp <= 0:
            return False


def solve():
    min_cost = float("inf")
    max_cost = 0
    for w, a, r1, r2 in all_combinations:
        cost = get_cost(w, a, r1, r2)
        damage = get_damage(w, a, r1, r2)
        armor = get_armor(w, a, r1, r2)
        if fight(damage, armor):
            min_cost = min(min_cost, cost)
        else:
            max_cost = max(max_cost, cost)
    return min_cost, max_cost


if __name__ == "__main__":
    t0 = time.time()

    part1_answer, part2_answer = solve()

    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time() - t0)
