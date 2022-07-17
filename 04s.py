from time import time

INPUT = "inputs/04big.txt"

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

def part12(nums, boards):
    eboards = [[board, 0] for board in boards]
    bingodBoards = []
    flag = True
    for num in nums:
        for board in eboards:
            for row in board[0]:
                for n in row:
                    if num == n[0]:
                        n[1] = 1
            if checkBingo(board[0]) and not board[1] == 1:
                board[1] = 1
                bingodBoards.append(board[0])
                if flag:
                    print(f"part1: {calcScore(bingodBoards[0]) * num}")
                    flag = False
        if len(eboards) == len(bingodBoards):
            print(f"part2: {calcScore(bingodBoards[-1]) * num}")
            return

t0 = time()
nums, boards = parser()
part12(nums, boards)
print(f"took: {time()-t0}")