from time import time
import sys
INPUT = "inputs/09.txt"
sys.setrecursionlimit(5000)

def timer(func, *stuff, n=1):
    t0 = time()
    for i in range(n):
        out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((((time()-t0)/n)*1000), 3)} ms ave for {n} iteration{'s' if n != 1 else ''}")
    return out

def parser():
    def p(i):
        i = i.strip()
        return [int(c) for c in i]
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def checkLocalLow(x, y, grid):
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        xx, yy = x + dx, y + dy
        if 0 <= xx < len(grid) and 0 <= yy < len(grid[1]) and grid[xx][yy] <= grid[x][y]:
            return False
    return True 

def part1(input):
    count = 0
    for x in range(len(input)):
        for y in range(len(input[0])):
            if checkLocalLow(x, y, input):
                count += input[x][y]+1
    return count

def findBasinSize(x, y, grid, checked):
    out = 1
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        xx, yy = x + dx, y + dy
        if 0 <= xx < len(grid) and 0 <= yy < len(grid[1]) and grid[xx][yy] != 9 and checked[xx][yy] == False:
            checked[xx][yy] = True
            s, checked = findBasinSize(xx, yy, grid, checked)
            out += s
    return out, checked

def part2(input):
    ans = 1
    checked = [[False]*len(input[0]) for i in range(len(input))]
    basins = []
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] == 9:
                checked[x][y] = True
                continue
            if checked[x][y] == False:
                checked[x][y] = True
                b, checked = findBasinSize(x, y, input, checked)
                if b:
                    basins.append(b)
    for _ in range(3):
        ans *= basins.pop(basins.index(max(basins)))
    return ans


stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)