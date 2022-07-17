from time import time
import numpy as np

INPUT = "inputs/03.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    def p(i):
        return [int(j) for j in list(i.strip())]
    with open(INPUT) as f:
        return np.array(list(map(p, f.readlines())))

def part1(input):
    gamma = ""
    for i in range(len(input[0])):
        count1 = np.sum(input[:, i])
        count0 = len(input) - count1
        gamma += "1" if count1 > count0 else "0"
    igamma = int(gamma, 2)
    iepsilon = int("1"*len(gamma), 2) ^ igamma
    return igamma * iepsilon

def recursive_rem(input, rem, i=0):
    if len(input) == 1:
        return "".join([str(i) for i in input[0]])

    count1 = np.sum(input[:, i])
    count0 = len(input) - count1
    new = []
    
    for each in input:
        # if 1s > 0s append the 1s else append 0s if rem swaps that around
        if each[i] == (1 if ((count1 >= count0) ^ rem) else 0):
            new.append(each) 
    return recursive_rem(np.array(new), rem, i+1)

def part2(input):
    oxy = recursive_rem(input, 1)
    co2 = recursive_rem(input, 0)
    ioxy = int(oxy, 2)
    ico2 = int(co2, 2)
    return ioxy * ico2



stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)