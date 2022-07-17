from time import time
from types import ClassMethodDescriptorType

INPUT = "inputs/10.txt"
OPENERS = "([{<"
CLOSERS = ")]}>"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    def p(i):
        return i.strip()
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def waitForClose(line, char=0, opens=""):
    success = True
    while len(line):
        if not success:
            return False, line, opens
        if (l := line[0]) in CLOSERS:
            if not char:
                return False, line, opens
            if CLOSERS.index(l) == OPENERS.index(char):
                return True, line[1:], opens[:-1]
            else:
                return False, line, opens
        if line[0] in OPENERS:
            opens += line[0]
            success, line, opens = waitForClose(line[1:], line[0], opens)
    return (not len(line) and not len(opens)), "", opens


def part(input):
    fails = []
    incompletes = []
    for line in input:
        if (c := line[0]) in OPENERS:
            success, rest, opens = waitForClose(line)
            if success:
                print(line)
                pass
            elif len(rest):
                fails += [rest[0]]
            else:
                incompletes += [(line, opens)]
    return fails, incompletes

def part1(input):
    A = lambda x: {")":3,"]":57,"}":1197,">":25137}[x]
    fails, _ = part(input)
    return sum([A(f) for f in fails])

def part2(input):
    A = lambda x: {"(":1,"[":2,"{":3,"<":4}[x]
    scores = []
    _, missing = part(input)
    for _, m in missing:
        score = 0
        for c in m[::-1]:
            score *= 5
            score += A(c)
        scores += [score]
    scores.sort()
    return scores[len(scores)//2]

stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)