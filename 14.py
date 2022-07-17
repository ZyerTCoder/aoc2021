from time import time
from collections import Counter

INPUT = "inputs/14.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    with open(INPUT) as f:
        poly, rules = f.read().split("\n\n")
        return poly, dict(l.split(" -> ") for l in rules.split("\n"))

def countChars(s):
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

def buildPolyHard(poly, rules, steps):
    for _ in range(steps):
        print(_)
        for i in range(len(poly)-1):
            pair = "".join([poly[i*2:i*2+2]])
            poly = poly[:i*2+1] + rules[pair] + poly[i*2+1:]
        print(countChars(poly))
    return poly

def buildPoly(poly, rules, steps):
    pairs = Counter()
    for i in range(len(poly)-1):
        pairs[poly[i:i+2]] += 1
    for _ in range(steps):
        newCounter = pairs.copy()
        for key in pairs:
            letter = rules[key]
            newCounter[key[0]+letter] += pairs[key]
            newCounter[letter+key[1]] += pairs[key]
            newCounter[key] -= pairs[key]
        pairs = newCounter
    letterCount = Counter()
    for pair in pairs:
        letterCount[pair[0]] += pairs[pair]
    letterCount[poly[-1]] += 1
    ordered = letterCount.most_common()
    return ordered[0][1] - ordered[-1][1]

def part1(poly, rules):
    return buildPoly(poly, rules, 10)

def part2(poly, rules):
    return buildPoly(poly, rules, 40)


poly, rules = timer(parser)
timer(part1, poly, rules)
timer(part2, poly, rules)