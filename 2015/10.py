import time


def look_and_say(seq):
  result = ""
  prev = seq[0]
  amount = 1
  for x in seq[1:]:
    if x == prev:
      amount+=1
    else:
      result += str(amount) + prev
      prev = x
      amount = 1
  result += str(amount) + prev
  return result

def part1(indata):
  seq = indata
  for i in range(40):
    seq = look_and_say(seq)
  return len(seq)


def part2(indata):
  seq = indata
  for i in range(50):
    seq = look_and_say(seq)
  return len(seq)



if __name__ == "__main__":
  indata = "1321131112"
  t0 = time.time()

  print("part1:", part1(indata))
  print("part2:", part2(indata))

  print("time:", time.time()-t0)
