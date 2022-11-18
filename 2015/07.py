import time

def resolve(key, cables):
  if isinstance(key, int):
    return key
  
  if isinstance(key, str):
    if key.isdigit():
      return int(key)
    else:
      res = resolve(cables[key], cables)
      cables[key] = res
      return res
  
  if len(key) == 2:
    x = resolve(key[1], cables)
    return x ^ 65535 # not operator
  elif len(key) == 3:
    x = resolve(key[0], cables)
    operator = key[1]
    y = resolve(key[2], cables)
    res = 0
    if operator == 'AND':
      res = x & y
    elif operator == 'OR':
      res = x | y
    elif operator == 'RSHIFT':
      res = x >> y
    elif operator == 'LSHIFT':
      res = x << y
    else:
      print("invalid operator")
    return res
  else:
    print("invalid tuple length")

def part1(indata):
  # Init dict
  cables = dict()
  for line in indata:
    line = line.split(" ")
    match len(line):
      case 3: # value assignment
        cables[line[2]] = line[0]
      case 4: # not operator
        cables[line[3]] = ('not', line[1])
      case 5: # all other operators
        cables[line[4]] = (line[0], line[1], line[2])
  
  # Resolve values
  for key in cables.keys():
    resolve(key, cables)

  return cables['a']

def part2(indata, part1_result):
  # Init dict
  cables = dict()
  for line in indata:
    line = line.split(" ")
    match len(line):
      case 3: # value assignment
        cables[line[2]] = line[0]
      case 4: # not operator
        cables[line[3]] = ('not', line[1])
      case 5: # all other operators
        cables[line[4]] = (line[0], line[1], line[2])
  
  cables['b'] = part1_result

  # Resolve values
  for key in cables.keys():
    resolve(key, cables)

  return cables['a']

if __name__ == "__main__":
  t0 = time.time()
  with open("input/07", "r") as f:
    indata = f.read().split('\n')

  part1_result = part1(indata)
  print("part1:", part1(indata))
  print("part2:", part2(indata, part1_result))

  print("time:", time.time()-t0)
