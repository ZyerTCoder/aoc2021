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
        return i.strip()
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def part1(input):
    gamma = ""
    epsilon = ""
    for i in range(len(input[0])):
        count1 = 0
        count0 = 0
        for n in input:
            if n[i] == "0":
                count0 += 1
            elif n[i] == "1":
                count1 += 1
            else:
                print(n[i])
                print("wtf")
        if count0 > count1:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    igamma = int(eval('0b' + gamma))
    iep = int(eval('0b' + epsilon))
    print(f"e: {iep} g: {igamma}")
    return igamma * iep

def logical_xor(a, b):
    return not b if a else bool(b)

def recursive_rem(input, rem, i=0):
    #print(f"input length: {len(input)} i={i}")
    #print(f"input: {input}")
    new = []
    if len(input) == 1:
        return input[0]
    count0 = 0
    count1 = 0
    for n in input:
        if n[i] == "0":
            count0 += 1
        elif n[i] == "1":
            count1 += 1
        else:
            print(f"wtf: {n[i]}")
    #print(f"count1: {count1} count0: {count0}")
    if rem:
        if count1 >= count0:
            for each in input:
                if each[i] == "1":
                    new.append(each)
        else:
            for each in input:
                if each[i] == "0":
                    new.append(each)
    else:
        if count1 >= count0:
            for each in input:
                if each[i] == "0":
                    new.append(each)
        else:
            for each in input:
                if each[i] == "1":
                    new.append(each)
    return recursive_rem(new, rem, i+1)

def part2(input):
    oxy = recursive_rem(input, 1)
    co2 = recursive_rem(input, 0)
    ioxy = int(eval('0b' + oxy))
    ico2 = int(eval('0b' + co2))
    #print(ioxy)
    return ioxy * ico2
    
def part3(inp):
    input = inp
    for i in range(len(input[0])):
        print(f"input length: {len(input)} i={i}")
        print(input)
        if len(input) == 1:
            break
        count0 = 0
        count1 = 0
        for n in input:
            if n[i] == "0":
                count0 += 1
            elif n[i] == "1":
                count1 += 1
            else:
                print(f"wtf: {n[i]}")
        print(f"count1: {count1} count0: {count0}")
        if count1 >= count0:
            for each in input:
                if each[i] == "0":
                    input.remove(each)
        else:
            for each in input:
                if each[i] == "1":
                    input.remove(each)
    return int(eval('0b' + input[0]))


stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)
#timer(part3, stuff)