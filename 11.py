from time import time
import sys
from copy import deepcopy as copy

sys.setrecursionlimit(5000)
INPUT = "inputs/11.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    def p(s):
        return [int(i) for i in s.strip()]
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def increase(r,c,input, notflashed):
    inBounds=lambda x,y:0<=x<L and 0<=y<Q
    surrounding=lambda x,y:[(x,y+1),(x+1,y),(x,y-1),(x-1,y),(x+1,y+1),(x+1,y-1),(x-1,y-1),(x-1,y+1)]
    input[r][c] += 1
    if input[r][c] > 9 and notflashed[r][c]:
        notflashed[r][c] = 0
        for x, y in surrounding(r,c):
            if inBounds(x,y):
                input, notflashed = increase(x,y,input, notflashed)
    return input, notflashed

def step(input):
    notflashed=[[1]*len(input[0]) for _ in range(len(input))]
    for r in range(len(input)):
        for c in range(len(input[0])):
            input, notflashed = increase(r,c, input, notflashed)
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] > 9:
                input[r][c] = 0
    return input, (len(input)*len(input[0]))-sum([sum(row) for row in notflashed])

def part1(input, cycles):
    input = copy(input)
    flashes = 0
    for i in range(cycles):
        input, nflashes = step(input)
        flashes += nflashes
    return flashes

def part2(input):
    input = copy(input)
    i = 0
    while 1:
        i += 1
        input, nflashes = step(input)
        if nflashes == len(input)*len(input[0]):
            return i
    return


stuff = timer(parser)
L,Q=len(stuff),len(stuff[0])


timer(part1, stuff, 100)
timer(part2, stuff)