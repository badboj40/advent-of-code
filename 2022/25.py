# 25   01:22:56   3042      0   01:22:57   2401      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR, DAY = 2022, 25
puzzle = Puzzle(day=DAY, year=YEAR)
indata = puzzle.input_data.split('\n')


def snafu2decimal(snafu):
  decimal = 0
  for i, digit in enumerate(reversed(snafu)):
    match digit:
      case '-':
        d = -1
      case '=':
        d = -2
      case _:
        d = int(digit)
    decimal += 5**i * d
  return decimal


def decimal2snafu(decimal):
  snafu = ""
  while decimal > 0:
    remainder = decimal % 5
    decimal //= 5
    match remainder:
      case 0 | 1 | 2:
        snafu = str(remainder) + snafu
      case 3:
        snafu = '=' + snafu
        decimal += 1
      case 4:
        snafu = '-' + snafu
        decimal += 1
  return snafu

  
if __name__ == "__main__":
  t0 = time.time()
  decimal_sum = sum(snafu2decimal(snafu) for snafu in indata)
  snafu_sum = decimal2snafu(decimal_sum)
  submit(snafu_sum, part="a", day=DAY, year=YEAR)
  print("\ntime:", time.time()-t0)