from copy import deepcopy

p1_start = 10
p2_start = 2


class Player:
    def __init__(self, pos):
        self.pos = pos
        self.score = 0

    def move(self, steps):
        self.pos += steps
        while self.pos > 10:
            self.pos -= 10
        self.score += self.pos


def part1():
    p1 = Player(p1_start)
    p2 = Player(p2_start)
    die = 1
    turn = 'p1'
    rolls = 0
    while p1.score < 1000 and p2.score < 1000:
        steps = 0
        for i in range(3):
            steps += die
            die += 1
            rolls += 1
            while die > 100:
                die -= 100
        if turn == 'p1':
            p1.move(steps)
            turn = 'p2'
        else:
            p2.move(steps)
            turn = 'p1'
    return min(p1.score, p2.score) * rolls


def move_single(state, steps):
    p1_pos, p1_score, p2_pos, p2_score, turn = state
    if turn == 'p1':
        p1_pos += steps
        if p1_pos > 10:
            p1_pos -= 10
        p1_score += p1_pos
        turn = 'p2'
    else:
        p2_pos += steps
        if p2_pos > 10:
            p2_pos -= 10
        p2_score += p2_pos
        turn = 'p1'
    new_state = (p1_pos, p1_score, p2_pos, p2_score, turn)
    return new_state


def move_quantum(state, occurances):
    new_states = dict()
    new_states[move_single(state, 3)] = 1 * occurances
    new_states[move_single(state, 4)] = 3 * occurances
    new_states[move_single(state, 5)] = 6 * occurances
    new_states[move_single(state, 6)] = 7 * occurances
    new_states[move_single(state, 7)] = 6 * occurances
    new_states[move_single(state, 8)] = 3 * occurances
    new_states[move_single(state, 9)] = 1 * occurances
    return new_states


def part2():
    p1_wins = 0
    p2_wins = 0
    first_state = (p1_start, 0, p2_start, 0, 'p1') # p1_pos, p1_score, p2_pos, p2_score, turn

    current_states = {first_state : 1}

    while current_states:
        next_gen = dict()
        for current_state in current_states:
            current_occurances = current_states[current_state]
            new_states = move_quantum(current_state, current_occurances)
            for state in new_states:
                occurances = new_states[state]
                if state[1] >= 21:
                    p1_wins += occurances
                elif state[3] >= 21:
                    p2_wins += occurances
                elif state not in next_gen:
                    next_gen[state] = occurances
                else:
                    next_gen[state] += occurances
        current_states = next_gen

    return max(p1_wins, p2_wins)


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
