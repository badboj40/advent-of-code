from copy import deepcopy

with open("input/6", "r") as f:
    indata = [int(x) for x in f.read().split(',')]


def population_after_days(population_input, days):
    population = deepcopy(population_input)
    for _ in range(days):
        new_fish = 0
        for i, x in enumerate(population):
            if x == 0:
                new_fish += 1
                population[i] = 6
            else:
                population[i] -= 1
        population.extend([8] * new_fish)
    return len(population)


def population_after_days2(population_input, days):
    population = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for fish in population_input:
        population[fish] += 1
    for _ in range(days):
        new_fish = population[0]
        for i in range(8):
            population[i] = population[i+1]
        population[6] += new_fish
        population[8] = new_fish
    return sum(population.values())


print(f"part1: {population_after_days2(indata,80)}")
print(f"part2: {population_after_days2(indata,256)}")
