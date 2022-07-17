from time import time

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
    flagRows = False
    flagCols = False
    for row in board:
        flag = True
        for n in row:
            if n[1] == 0:
                flag = False
        if flag:
            flagRows = True
    for col in range(len(board[0])):
        flag = True
        for row in board:
            if row[col][1] == 0:
                flag = False
        if flag:
            flagCols = True
    return (flagCols or flagRows)

def calcScore(board):
    t = 0
    for row in board:
        for n in row:
            if n[1] == 0:
                t += n[0]
    return t

def part1(nums, boards):
    for num in nums:
        for board in boards:
            for row in board:
                for n in row:
                    if num == n[0]:
                        n[1] = 1
            if checkBingo(board):
                return calcScore(board) * num

def part2(nums, boards):
    eboards = [[board, 0] for board in boards]
    for num in nums:
        t = len(eboards)
        for board in eboards:
            for row in board[0]:
                for n in row:
                    if num == n[0]:
                        n[1] = 1
            if checkBingo(board[0]):
                t -= 1
                if t == 1:
                    for board in eboards:
                        if board[1] == 0:
                            board[1] = 2
                if board[1] == 0:
                    board[1] = 1
                if t == 0:
                    for board in eboards:
                        if board[1] == 2:
                            return calcScore(board[0]) * num


nums, boards = timer(parser)
timer(part1, nums, boards)
timer(part2, nums, boards)