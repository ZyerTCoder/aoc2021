from time import time

t0 = time()
f = open("inputs/02.txt")

def parser(file):
    return [i.split(" ") for i in file.read().strip().split("\n")]

def part1(input):
    forward = 0
    for e in input:
        if e[0] == "forward":
            forward += int(e[1])
    up = 0
    for e in input:
        if e[0] == "up":
            up += int(e[1])
    down = 0
    for e in input:
        if e[0] == "down":
            down += int(e[1])
    return forward * (down - up)

def part2(input):
    aim = 0
    forward = 0
    depth = 0
    for e in input:
        if e[0] == "down":
            aim += int(e[1])
        if e[0] == "up":
            aim -= int(e[1])
        if e[0] == "forward":
            forward += int(e[1])
            depth += int(e[1]) * aim
    return forward * depth

stuff = parser(f)
print(f"part1: {part1(stuff)}")
print(f"part2: {part2(stuff)}")
print(f"time: {round((time()-t0)*1000, 3)} ms")