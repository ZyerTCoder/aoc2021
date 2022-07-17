from time import time

INPUT = "inputs/02.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    def p(i):
        x, y = i.split(" ")
        return x, int(y)
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def part1(input):
    forward, depth = 0, 0
    for e in input:
        if e[0] == "forward":
            forward += e[1]
        if e[0] == "up":
            depth -= e[1]
        if e[0] == "down":
            depth += e[1]
    return forward * depth

def part2(input):
    aim, forward, depth = 0, 0, 0
    for e in input:
        if e[0] == "down":
            aim += e[1]
        if e[0] == "up":
            aim -= e[1]
        if e[0] == "forward":
            forward += e[1]
            depth += e[1] * aim
    return forward * depth

stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)