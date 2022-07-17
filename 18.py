from time import perf_counter as pf
import json
import copy

INPUT = "inputs/18l.txt"

def timer(func):
    N = 1
    def wrapper(*args, **kwargs):
        t0 = pf()
        for _ in range(N):
            out = func(*args, **kwargs)
        tf = pf()
        print(f"{func.__name__}: " + (f"{out}" if len(args) else ""))
        print(f"  time: {round(((tf-t0)*1000)/N, 3)} ms")
        return out
    return wrapper

@timer
def parser():
    def p(i):
        return i.strip()
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def split(hw):
    # text = json.dumps(hw, separators=(",", ":"))
    # if text[0] == '"' or text[0] == "'":
    #     text = text[1:-1] #idk why it was adding "" around the json string
    text = hw
    # print("orig", text)
    bigIndex = None
    for i, c in enumerate(text):
        if c not in "[]," and text[i+1] not in "[],":
            bigIndex = i
            break

    if bigIndex:
        bigNum = int(text[bigIndex:bigIndex+2])
        left = bigNum//2
        right = bigNum-left
        newString = text[:bigIndex] + f"[{left},{right}]" + text[bigIndex+2:]
        return True, newString
    
    return False, hw

def explode(hw):
    # text = json.dumps(hw, separators=(",", ":"))
    # if text[0] == '"' or text[0] == "'":
    #     text = text[1:-1]
    text = hw

    depth = 0
    skip = False
    pastExplosion = False
    leftIndex = None
    rightIndex = None
    explodeStart = None
    explodeEnd = None
    for i, c in enumerate(text):
        if skip: 
            skip = False
            continue
        elif c not in "[]," and text[i+1] not in "[],":
            skip = True
        if depth > 4 and not explodeStart:
            explodeStart = i
            pastExplosion = True
        if explodeStart and not explodeEnd:
            if depth < 5:
                explodeEnd = i - 1
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        if not (explodeStart and not explodeEnd) and c not in "[],":
            if not pastExplosion:
                leftIndex = i
            else:
                if not rightIndex:
                    rightIndex = i
    if not explodeStart:
        return False, text
    explodedBits = [int(i) for i in text[explodeStart:explodeEnd].split(",")]
    indexOffset = [0,0,0,0]
    newLeft = None
    newRight = None
    if leftIndex:
        if text[leftIndex+1] in "[],":
            newLeft = int(text[leftIndex]) + explodedBits[0]
        else:
            newLeft = int(text[leftIndex:leftIndex+2]) + explodedBits[0]
            indexOffset[0] = 1
    if rightIndex:
        if text[rightIndex+1] in "[],":
            newRight = int(text[rightIndex]) + explodedBits[1]
        else:
            newRight = int(text[rightIndex:rightIndex+2]) + explodedBits[1]
            indexOffset[3] = 1

    newString1 = text
    if newRight:
        newString1 = text[:rightIndex] + str(newRight) + text[rightIndex+indexOffset[3]+1:]
    newString2 = newString1[:explodeStart-1] + "0" + newString1[explodeEnd+1:]
    newString3 = newString2
    if newLeft:
        newString3 = newString2[:leftIndex] + str(newLeft) + newString2[leftIndex+indexOffset[0]+1:]

    # print("indexes:", leftIndex, explodeStart, explodeEnd, rightIndex)
    # print("new numbers", newLeft, newRight)
    # print("old0", text)
    # print("new1", newString1)
    # print("new2", newString2)
    # print("new3", newString3)
    # exit()
    return True, newString3

def sumFinal(hw):
    for i, each in enumerate(hw):
        if isinstance(each, list):
            hw[i] = sumFinal(each)
    return hw[0]*3 + hw[1]*2

def reduce(hw):
    while True:
        exploded, hw = explode(hw)
        # if exploded:
        #     print("postexplo", hw)
        if not exploded:
            spilteded, hw = split(hw)
            # if spilteded:
            #     print("postsplit", hw)
            if not spilteded:
                return hw

    
@timer
def part1(input):
    first = input[0]
    for i in range(1, len(input)):
        second = input[i]
        first = reduce(f"[{first},{second}]")
    hw = json.loads(first)
    return sumFinal(hw)

@timer
def part2(input):
    largest = 0
    for i in range(len(input)):
        for j in range(i, len(input)):
            first = input[i]
            second = input[j]
            tmp = reduce(f"[{first},{second}]")
            sumf = sumFinal(json.loads(tmp))
            if sumf > largest:
                largest = sumf
    return largest


stuff = parser()
part1(stuff)
part2(stuff)