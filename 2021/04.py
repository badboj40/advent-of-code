from copy import deepcopy
with open("input/04", "r") as f:
    indata = f.read().split('\n')

boards = []
numbers = [int(x) for x in indata[0].split(',')]

board = []
for line in indata[2:]:
    if line:
        board.append([int(x) for x in line.split()])
    else:
        boards.append(board)
        board = []


def check_number(board, number):
    for row in board:
        for i in range(5):
            if row[i] == number:
                row[i] = 0
    return board


def has_bingo(board):
    for row in board:
        if sum(row) == 0:
            return True
    for i in range(5):
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == 0:
            return True
    return False


def board_score(board, n):
    summ = 0
    for row in board:
        summ += sum(row)
    return summ * n


def part1(input_boards):
    boards = deepcopy(input_boards)
    for n in numbers:
        for i in range(len(boards)):
            boards[i] = check_number(boards[i], n)
            if has_bingo(boards[i]):
                return board_score(boards[i], n)


def part2(input_boards):
    boards = deepcopy(input_boards)
    for n in numbers:
        losing_boards = []
        for i in range(len(boards)):
            boards[i] = check_number(boards[i], n)
            if not has_bingo(boards[i]):
                losing_boards.append(boards[i])
            elif len(boards) == 1:
                return board_score(boards[i], n)
        boards = losing_boards


print(f"part1: {part1(boards)}")
print(f"part2: {part2(boards)}")

