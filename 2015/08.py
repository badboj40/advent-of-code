import time

def part1(indata):
  result = 0
  for row in indata:
    escaped_string = row.encode().decode('unicode-escape')
    result += 2 + len(row) - len(escaped_string)
  return result

def part2(indata):
  result = 0
  for string in indata:
    result += 2
    for char in string:
      if char == '"' or char == '\\':
        result += 1
  return result

if __name__ == "__main__":
  with open("input/08", "r") as f:
    indata = f.read().split('\n')

  t0 = time.time()

  print("part1:", part1(indata))
  print("part2:", part2(indata))

  print("time:", time.time()-t0)
