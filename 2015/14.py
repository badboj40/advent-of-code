import time

TRAVEL_TIME = 2503


def parse_input():
  with open("input/14", "r") as f:
    indata = f.read().split('\n')

  reindeers = dict()

  for row in indata:
    l = row.split(' ')
    reindeer = l[0]
    speed = int(l[3])
    flying_duration = int(l[6])
    resting_duration = int(l[-2])

    reindeer_data = [speed for x in range(flying_duration)] + \
                    [0 for x in range(resting_duration)]

    reindeers[reindeer] = reindeer_data
  return reindeers


def part1(indata):
  score = dict()
  for reindeer in indata.keys():
    score[reindeer] = 0
  for i in range(TRAVEL_TIME):
    for reindeer in indata.keys():
      score[reindeer] += indata[reindeer][i%len(indata[reindeer])]
  
  return score[max(score, key=score.get)]


def part2(indata):
  distance = dict()
  score = dict()
  for reindeer in indata.keys():
    distance[reindeer] = 0
    score[reindeer] = 0
  for i in range(TRAVEL_TIME):
    for reindeer in indata.keys():
      distance[reindeer] += indata[reindeer][i%len(indata[reindeer])]
    score[max(distance, key=distance.get)] += 1
  
  return score[max(score, key=score.get)]


if __name__ == "__main__":
  print() 
  t0 = time.time()
  indata = parse_input()

  print("part1:", part1(indata))
  print("part2:", part2(indata))

  print("time:", time.time()-t0)
