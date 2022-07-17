from time import time

INPUT = "inputs/09.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    def p(i):
        i = i.strip()
        return [int(c) for c in i]
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def checkLocalLow(x, y, grid):
    low = True
    try:
        if grid[x+1][y] <= grid[x][y]:
            return False
    except IndexError as e:
        pass
    try:
        if grid[x-1][y] <= grid[x][y]:
            return False
    except IndexError as e:
        pass
    try:
        if grid[x][y+1] <= grid[x][y]:
            return False
    except IndexError as e:
        pass
    try:
        if grid[x][y-1] <= grid[x][y]:
            return False
    except IndexError as e:
        pass
    return True  

def part1(input):
    count = 0
    for x in range(len(input)):
        for y in range(len(input[0])):
            if checkLocalLow(x, y, input):
                count += input[x][y]+1
    return count

def findBasinSize(x, y, grid, checkedLocs):
    out = 1
    try:
        if grid[x+1][y] != 9 and ((x+1, y) not in checkedLocs):
            checkedLocs += [(x+1, y)]
            s, checkedLocs = findBasinSize(x+1, y, grid, checkedLocs)
            out += s
    except IndexError as e:
        pass
    try:
        if x-1>=0 and grid[x-1][y] != 9 and ((x-1, y) not in checkedLocs):
            checkedLocs += [(x-1, y)]
            s, checkedLocs = findBasinSize(x-1, y, grid, checkedLocs)
            out += s
    except IndexError as e:
        pass
    try:
        if grid[x][y+1] != 9 and ((x, y+1) not in checkedLocs):
            checkedLocs += [(x, y+1)]
            s, checkedLocs = findBasinSize(x, y+1, grid, checkedLocs)
            out += s
    except IndexError as e:
        pass
    try:
        if y-1>=0 and grid[x][y-1] != 9 and ((x, y-1) not in checkedLocs):
            checkedLocs += [(x, y-1)]
            s, checkedLocs = findBasinSize(x, y-1, grid, checkedLocs)
            out += s
    except IndexError as e:
        pass
    return out, checkedLocs

def part2(input):
    ans = 1
    checked = []
    basins = []
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] == 9:
                checked += (x, y)
                continue
            if (x, y) not in checked:
                checked += [(x, y)]
                b, checked = findBasinSize(x, y, input, checked)
                if b:
                    basins.append(b)
    for i in range(3):
        ans *= basins.pop(basins.index(max(basins)))
    return ans


stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)