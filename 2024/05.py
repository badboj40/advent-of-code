#  5   00:11:28  1692      0   00:18:08  1292      0

from aocd.models import Puzzle
import time


def is_ok(page, order_rules):
    for x,y in order_rules:
        if x in page and y in page and page.index(y) < page.index(x):
            return False
    return True


def fix_page(page, order_rules):
    while not is_ok(page, order_rules):
        for x, y in order_rules:
            if x in page and y in page and (j:=page.index(y)) < (i:=page.index(x)):
                page[i], page[j] = y, x
    return page


def part1(order_rules, pages):
    ok_pages = [page for page in pages if is_ok(page, order_rules)]
    return sum(page[len(page)//2] for page in ok_pages)


def part2(order_rules, pages):
    not_ok_pages = [page for page in pages if not is_ok(page, order_rules)]
    fixed_pages = [fix_page(page, order_rules) for page in not_ok_pages]
    return sum(page[len(page)//2] for page in fixed_pages)


if __name__ == "__main__":
    t0 = time.time()

    directory, filename = __file__.split('/')[-2:]
    YEAR, DAY = int(directory), int(filename[:-3])

    puzzle = Puzzle(day=DAY, year=YEAR)
    puzzle_input = puzzle.input_data.split("\n\n")

    order_rules = [[*map(int,row.split('|'))] for row in puzzle_input[0].split('\n')]
    pages       = [[*map(int,row.split(','))] for row in puzzle_input[1].split('\n')]

    print("\npart1:", part1(order_rules, pages))
    print("\npart2:", part2(order_rules, pages))
    print("\ntime:", time.time()-t0)