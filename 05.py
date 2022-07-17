from time import time
from types import NoneType
from timeit import timeit

INPUT = "inputs/05.txt"

def timer(func, *stuff, n=1):
    t0 = time()
    for i in range(n):
        out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    def p(i):
        return [[int(b) for b in a.split(",")] for a in i.strip().split(" -> ")]
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def findMax(input):
    o = 0
    for line in input:
        for point in line:
            if (m := max(point)) > o:
                o = m
    return o
    
def genPoints(start, end, part2=False):
    if start[0] <= end[0]:
        xPoints = list(range(start[0], end[0]+1))
    else: 
        xPoints = list(range(start[0], end[0]-1, -1))
    if start[1] <= end[1]:
        yPoints = list(range(start[1], end[1]+1))
    else:
        yPoints = list(range(start[1], end[1]-1, -1))
    if (c := len(xPoints) - len(yPoints))> 0:
        return [[x, yPoints[0]] for x in xPoints]
    elif c < 0:
        return [[xPoints[0], y] for y in yPoints]
    elif c == 0 and part2:
        return[[x, y] for x, y in zip(xPoints, yPoints)]
    else:
        return []

def part1(input):
    max = findMax(input) + 1
    grid = [[0]*max for n in range(max)]
    for line in input:
        points = genPoints(line[0], line[1])
        if points == []:
            continue
        for p in points:
            grid[p[1]][p[0]] += 1
    o = 0
    for line in grid:
        for p in line:
            if p>1:
                o += 1
    return o

def part2(input):
    size = max([max(map(max, l)) for l in input]) + 1
    grid = [[0]*size for n in range(size)]
    for line in input:
        points = genPoints(line[0], line[1], True)
        for p in points:
            grid[p[1]][p[0]] += 1
    o = 0
    for line in grid:
        for p in line:
            if p>1:
                o += 1
    return o


stuff = timer(parser)
timer(part1, stuff, n=10000)
timer(part2, stuff, n=10000)