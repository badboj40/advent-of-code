import time

def parse_input():
  with open("input/01", "r") as f:
    indata = f.read().split('\n')
  return indata

def part1(indata):
  calories = []
  cals = 0
  for row in indata:
    if row:
      cals += int(cals)
    else:
      calories.append(cals)
      cals = 0
  return max(calories)


def part2(indata):
  calories = []
  cals = 0
  for row in indata:
    if row:
      cals += int(row)
    else:
      calories.append(cals)
      cals = 0
  calories.sort()
  return sum(calories[-3:])


if __name__ == "__main__":
  print() 
  t0 = time.time()
  indata = parse_input()

  print("part1:", part1(indata))
  print("part2:", part2(indata))

  print("time:", time.time()-t0)
