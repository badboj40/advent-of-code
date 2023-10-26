from aocd.models import Puzzle
from aocd import submit
from queue import PriorityQueue
import re
import time
import copy

directory, filename = __file__.split('/')[-2:]
YEAR, DAY = int(directory), int(filename[:-3])

puzzle = Puzzle(day=DAY, year=YEAR)

BOSS_HP, BOSS_DAMAGE = map(int, re.findall(r"\d+", puzzle.input_data))
PLAYER_HP, PLAYER_MANA = 50, 500

spell_data = {
    # name            cost, damage, armor, heal, mana, duration]
    "Magic Missile": [53,   4,      0,     0,    0,    1],
    "Drain":         [73,   2,      0,     2,    0,    1],
    "Shield":        [113,  0,      7,     0,    0,    6],
    "Poison":        [173,  3,      0,     0,    0,    6],
    "Recharge":      [229,  0,      0,     0,    101,  5],
}


class Spell:
    def __init__(self, name):
        cost, damage, armor, heal, mana, duration = spell_data[name]
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.heal = heal
        self.mana = mana
        self.duration = duration
    
    def __eq__(self, other):
        return self.name == other.name


class State:
    def __init__(self):
        self.player_hp = PLAYER_HP
        self.mana = PLAYER_MANA
        self.boss_hp = BOSS_HP
        self.spells = []
        self.mana_spent = 0
        self.turn = "player"

    def is_valid(self):
        return self.player_hp > 0 and self.boss_hp > 0 and self.mana >= 0

    def effects(self):
        for spell in self.spells:
            self.boss_hp -= spell.damage
            self.player_hp += spell.heal
            self.mana += spell.mana
            spell.duration -= 1
        self.spells = [spell for spell in self.spells if spell.duration > 0]

    def cast_spell(self, spell_name):
        spell = Spell(spell_name)
        if spell.cost > self.mana or spell in self.spells:
            return False
        self.spells.append(spell)
        self.mana_spent += spell.cost
        self.mana -= spell.cost
        return self.is_valid()

    def get_new_states(self):
        new_states = []
        self.turn = "boss"
        for spell_name in spell_data:
            new_state = copy.deepcopy(self)
            success = new_state.cast_spell(spell_name)
            if success:
                new_states.append(new_state)
        return new_states

    def do_turn(self):
        if self.turn == "player":
            return self.get_new_states()
        self.boss_attack()
        return [self] if self.is_valid() else []

    def boss_attack(self):
        damage = max(1, BOSS_DAMAGE -
                     sum(spell.armor for spell in self.spells))
        self.player_hp -= damage
        self.turn = "player"

    def __lt__(self, other):
        # Used for priority queque sorting
        return self.mana_spent * self.boss_hp < other.mana_spent * other.boss_hp


def solve(hard_mode=False):
    pq = PriorityQueue()
    pq.put(State())

    # Evaluate the best states first
    while not pq.empty():
        state = pq.get()

        # Apply hard mode rules
        state.player_hp -= hard_mode and state.turn == "player"
        if not state.is_valid():
            continue

        state.effects()

        # Check win - priority queque ensures this is the lowest mana spent
        if state.boss_hp <= 0:
            return state.mana_spent
        
        for new_state in state.do_turn():
            pq.put(new_state)
    return -1


if __name__ == "__main__":
    t0 = time.time()

    part1_answer = solve()
    print("\npart1:", part1_answer)
    submit(part1_answer, part="a", day=DAY, year=YEAR)

    part2_answer = solve(hard_mode=True)
    print("\npart2:", part2_answer)
    submit(part2_answer, part="b", day=DAY, year=YEAR)

    print("\ntime:", time.time()-t0)
