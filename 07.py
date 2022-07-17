from time import time

INPUT = "inputs/07.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    with open(INPUT) as f:
        return list(map(int, f.readline().split(",")))

def part1(input):
    t = float("inf")
    for i in range(len(input)):
        o = 0
        for crab in input:
            o += abs(crab - i)
        if o < t:
            t = o
        else:
            return t

def part2(input):   
    t = float("inf")
    for i in range(len(input)):
        o = 0
        for crab in input:
            n = abs(crab - i)
            o += n*(n+1)/2
        if o < t:
            t = o
        else:
            return int(t)


stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)