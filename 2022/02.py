from aocd.models import Puzzle
from aocd import submit
import time

YEAR = int('2022')
DAY = int('02')

def parse_input():
  puzzle = Puzzle(day=DAY, year=YEAR)
  indata = [x.split(' ') for x in puzzle.input_data.split('\n')]
  return indata

rock_paper_scissors = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 
                       'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

win_over = {'rock'    : 'scissors',
            'paper'   : 'rock', 
            'scissors': 'paper'}

move_score = {'rock': 1, 'paper': 2, 'scissors': 3}

def score_calc(opp, you):
  score = move_score[you]
  if win_over[you] == opp:
    score += 6 # win
  elif you == opp:
    score += 3 # draw
  return score


def part1(indata):
  score = 0
  for a, b in indata:
    opp = rock_paper_scissors[a]
    you = rock_paper_scissors[b]
    score += score_calc(opp, you)
  return score


def part2(indata):
  score = 0
  for a, b in indata:
    opp = rock_paper_scissors[a]
    if b == 'X': # lose
      you = win_over[opp]
    elif b == 'Y': # draw
      you = opp
    elif b == 'Z': # win
      for win, lose in win_over.items():
        if lose == opp:
          you = win
    score += score_calc(opp, you)
  return score


if __name__ == "__main__":
  print() 
  t0 = time.time()
  indata = parse_input()

  part1_answer = part1(indata)
  print("part1:", part1(indata))
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2(indata)
  print("part2:", part2(indata))
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("time:", time.time()-t0)
