from time import time

INPUT = "inputs/17.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    with open(INPUT) as f:
        s = f.read().strip()
        x, y = s.split(",")
        x = x[15:].split("..")
        y = y[3:].split("..")
        x = [int(i) for i in x]
        y = [int(i) for i in y]
        return [x, y]

def solve(input, negY=False):
    maxXspeed = 3 * max(input[0][0],input[0][1])
    maxYspeed = 3 * max(abs(input[1][0]), abs(input[1][1]))

    done = False
    i = 1
    startingSpeeds = []
    while not done:
        #print("====== i is", i)
        for speed in range(i):
            xvel = i - speed
            yvel = speed
            if negY:
                if yvel == 0:
                    continue
                yvel = -yvel
            startingVel = [xvel, yvel]
            #print(xvel, yvel)
            pos = [0, 0]
            step = 0
            #print("starting vel:", xvel, yvel)
            pastArea = False
            maxHeight = 0
            while xvel < maxXspeed and yvel < maxYspeed and not pastArea:
                pos[0] += xvel
                pos[1] += yvel
                if pos[1] > maxHeight:
                    maxHeight = pos[1]
                if xvel > 0:
                    xvel -= 1
                elif xvel < 0:
                    xvel += 1
                yvel -= 1
                step +=1
                if input[0][0] <= pos[0] <= input[0][1] and input[1][0] <= pos[1] <= input[1][1]:
                    startingSpeeds.append([startingVel[0], startingVel[1], maxHeight])
                if pos[0] > input[0][1] or pos[1] < min(input[1][1], input[1][0]):
                    pastArea = True
        if i > maxXspeed+maxYspeed:
            done = True
        i += 1
    maxHeight = 0
    for startingSpeed in startingSpeeds:
        if startingSpeed[2] > maxHeight:
            maxHeight = startingSpeed[2]
    #print(startingSpeeds)
    return maxHeight, startingSpeeds


def part1(input):
    p1, _ = solve(input)
    return p1

def part2(input):
    _, l1 = solve(input)
    _, l2 = solve(input, negY=True)
    lt = l1 + l2
    tmp = []
    for elem in lt:
        if elem not in tmp:
            tmp.append(elem)
    print(len(l1))
    return len(tmp)

stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)