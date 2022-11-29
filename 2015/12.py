import time
import json


def part1(indata):
  if isinstance(indata, int):
    return indata

  result = 0
  if isinstance(indata, list):
    for item in indata:
      result += part1(item)
  elif isinstance(indata, dict):
    for key in indata.keys():
      result += part1(indata[key])
  return result


def part2(indata):
  if isinstance(indata, int) or indata == "red":
    return indata

  result = 0
  if isinstance(indata, list):
    for item in indata:
      res = part2(item)
      if isinstance(res, int):
        result += res
  elif isinstance(indata, dict):
    for key in indata.keys():
      res = part2(indata[key])
      if not isinstance(res, int):
        return 0
      result += res
  return result

if __name__ == "__main__":
  with open("input/12", "r") as f:
    indata = json.loads(f.read())

  t0 = time.time()

  print("part1:", part1(indata))
  print("part2:", part2(indata))

  print("time:", time.time()-t0)
