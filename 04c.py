from time import time
from tqdm import tqdm

INPUT = "inputs/04big.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    with open(INPUT) as f:
        a = [i.strip() for i in f.read().strip().split("\n\n")]
        nums = [int(i) for i in a[0].split(",")]
        sboards = a[1:]
        boards = []
        for board in sboards:
            newb = []
            lines = board.split("\n")
            for line in lines:
                l = line.strip().split(" ")
                newl = []
                for j in l:
                    try:
                        newl.append([int(j), 0])
                    except ValueError:
                        pass
                newb.append(newl)
            boards.append(newb)
        return nums, boards

def checkBingo(board):
    for row in board:
        if sum([c[1] for c in row]) == len(row):
            return True
    for col in range(len(board[0])):
        if sum([row[col][1] for row in board]) == len(board[0]):
            return True

def calcScore(board):
    t = 0
    for row in board:
        for n in row:
            if n[1] == 0:
                t += n[0]
    return t

def part1(nums, boards):
    for num in tqdm(nums):
        for board in boards:
            for row in board:
                for n in row:
                    if num == n[0]:
                        n[1] = 1
            if checkBingo(board):
                return calcScore(board) * num

def part2(nums, boards):
    eboards = [[board, 0] for board in boards]
    bingodBoards = []
    for num in tqdm(nums):
        for board in eboards:
            for row in board[0]:
                for n in row:
                    if num == n[0]:
                        n[1] = 1
            if checkBingo(board[0]) and not board[1] == 1:
                board[1] = 1
                bingodBoards.append(board[0])
        if len(eboards) == len(bingodBoards):
            return calcScore(bingodBoards[-1]) * num

nums, boards = timer(parser)
timer(part1, nums, boards)
timer(part2, nums, boards)