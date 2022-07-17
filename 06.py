from time import time
from tqdm import tqdm

INPUT = "inputs/06.txt"

class Fish():
    def __init__(self, base, timer, count):
        self.base = base
        self.timer = timer
        self.count = count

    def update(self):
        if self.timer == 0:
            self.timer = 6
            return Fish(9, 9, self.count)
        self.timer -= 1
    
    def getTimer(self):
        return self.timer
    
    def increaseCount(self, n):
        self.count += n

    def getCount(self):
        return self.count

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    with open(INPUT) as f:
        return list(map(int, f.readline().split(",")))

def simulateFish(input, days):
    school = []
    for start in input:
        school.append(Fish(6, start, 1))
    for day in range(1, days + 1):
        for fish in school:
            if (new := fish.update()):
                school.append(new)
        new_school = []
        for fish in school:
            new_timers = [f.getTimer() for f in new_school]
            if t := fish.getTimer() in new_timers:
                for fish in new_school:
                    if t == fish.getTimer():
                        fish.increaseCount(fish.getCount())
            else:
                new_school.append(fish)
        school = new_school
    o = 0
    for fish in school:
        o += fish.getCount()
    return o

def simulateFishGood(input, days):
    school = [0]*9
    for t in [3,4,3,1,2]:
        school[t] += 1
    for day in range(days):
        new_school = [0]*9
        news = school[0]
        for t in range(8):
            new_school[t] = school[t+1]
        new_school[6] += news
        new_school[8] += news
        school = new_school
    return sum(school)

def part1(input):
    return simulateFishGood(input, 80)

def part2(input):
    return simulateFishGood(input, 256)

def part3(input):
    return simulateFishGood(input, 9999999)

def partmath(n):
    # implements a mathematical solution
    import numpy as np;
    init = np.array([0, 1, 1, 2, 1, 0, 0, 0, 0], 'O')
    tn = np.array([
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0]], 'O')
    a=np.sum(np.matmul(np.linalg.matrix_power(tn, n),init))

stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)
timer(partmath, 2**26)