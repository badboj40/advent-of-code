#  7   01:06:04   6697      0   01:23:25   7107      0

from aocd.models import Puzzle
from aocd import submit
import time

YEAR = int('2022')
DAY = int('07')


class Directory:
  def __init__(self, parent, name):
    self.parent = parent
    self.name = name
    self.children = []
    self.files = dict()
    self.size = 0
  
  def update_size(self):
    self.size = sum(self.files.values())
    for child in self.children:
      self.size += child.update_size()
    return self.size
  
  def traverse(self):
    total_size = 0
    if self.size <= 100000:
      total_size += self.size
    for child in self.children:
      total_size += child.traverse()
    return total_size
  
  def traverse2(self, size_needed, size_list):
    if self.size >= size_needed:
      size_list.append(self.size)
    for child in self.children:
      child.traverse2(size_needed, size_list)


def parse_input():
  puzzle = Puzzle(day=DAY, year=YEAR)
  indata = puzzle.input_data.split('\n')

  current_dir = Directory(-1, '/')
  for row in indata[1:]:
    if row == '$ ls': # listing directory contents is not relevant
      pass
    elif row[:4] == '$ cd': # change directory
      directory = row.split(' ')[-1]
      if directory == '..':
        current_dir = current_dir.parent
      else:
        for child in current_dir.children:
          if child.name == directory:
            current_dir = child
            break
    elif row[:3] == 'dir': # create file or directory
      directory_name = row.split(' ')[-1]
      new_dir = Directory(current_dir, directory_name)
      current_dir.children.append(new_dir)
    else:
      filesize, filename = row.split(' ')
      current_dir.files[filename] = int(filesize)
  
  # go to root
  while current_dir.parent != -1:
    current_dir = current_dir.parent

  return current_dir


def part1(directory):
  directory.update_size()
  total_size = directory.traverse()
  return total_size


def part2(directory):
  space_needed = 30000000 - (70000000 - directory.size)
  size_list = []
  directory.traverse2(space_needed, size_list)
  return min(size_list)


if __name__ == "__main__":
  indata = parse_input()
  t0 = time.time()

  part1_answer = part1(indata)
  print("\npart1:", part1_answer)
  submit(part1_answer, part="a", day=DAY, year=YEAR)

  part2_answer = part2(indata)
  print("\npart2:", part2_answer)
  submit(part2_answer, part="b", day=DAY, year=YEAR)

  print("\ntime:", time.time()-t0)
