from copy import deepcopy

# Target area:
x_min = 206
x_max = 250
y_min = -105
y_max = -57

# x_min = 20
# x_max = 30
# y_min = -10
# y_max = -5


def game_tick(pos, velocity):
    pos[0] += velocity[0]
    pos[1] += velocity[1]

    if velocity[0] < 0:
        velocity[0] += 1
    elif velocity[0] > 0:
        velocity[0] -= 1

    velocity[1] -= 1
    return pos, velocity


def has_failed(pos, velocity):
    if pos[1] < y_min: # below target
        return True
    if pos[0] > x_max: # to the right of target
        return True
    if velocity[0] == 0 and pos[0] < x_min: # did not reach the target
        return True
    return False


def part1():
    best_height = 0
    for x in range(250):
        for y in range(250):
            pos = [0, 0]
            velocity = [x, y]
            top_height = 0
            while not has_failed(pos, velocity):
                pos, velocity = game_tick(pos, velocity)
                top_height = max(top_height, pos[1])
                if x_min <= pos[0] <= x_max and y_min <= pos[1] <= y_max:
                    best_height = max(best_height, top_height)
                    break
    return best_height


def part2():
    target_hits = 0
    for x in range(260):
        for y in range(-110,250):
            pos = [0, 0]
            velocity = [x, y]
            top_height = 0
            while not has_failed(pos, velocity):
                pos, velocity = game_tick(pos, velocity)
                top_height = max(top_height, pos[1])
                if x_min <= pos[0] <= x_max and y_min <= pos[1] <= y_max:
                    target_hits += 1
                    break
    return target_hits


if __name__ == "__main__":
    print("part1:", part1())
    print("part2:", part2())
