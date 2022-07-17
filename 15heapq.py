from time import time
from math import sqrt
import heapq

INPUT = "inputs/15.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    def p(line):
        return [int(i) for i in line.strip()]
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

inBounds = lambda grid, r, c: 0<=r<len(grid) and 0<=c<len(grid[0])

def closest(opened):
    return min(zip(opened.values(), opened.keys()))[::-1]

def dijkstras(input):
    start = (0, 0)
    end = (len(input)-1, len(input[0])-1)
    done = False
    #opened = {start: sqrt((start[0]-end[0])**2 + (start[1]-end[1])**2)}
    opened = [(0, start)]
    
    #opened = {start: 0}
    closed = {}
    costsTo = {start: 0}
    linksdict = {}
    tfun = 0
    i = 0
    while not done:
        # take the open node with the closest value, remove it from the opened list and add it to the closed list
        node = heapq.heappop(opened)
        node = node[::-1]
        if node[0] == end:
            print("end reached")
            done = True
        closed[node[0]] = node[1]
        r, c = node[0]
        # add the adjancet nodes to the opened list
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            rr, cc = r + dr, c + dc
            if inBounds(input, rr, cc) and (rr, cc) not in closed:
                # add the new node to the open list with the cost of travelling to it, 
                # the value from the input, and the distance remaining (the heuristic)
                d = costsTo[node[0]] + input[rr][cc]# + sqrt((rr-end[0])**2 + (cc-end[1])**2)
                tf0 = time()
                # but why, this takes twice as long
                opened_reverse = {coords:value for value, coords in opened}
                tfun += time()-tf0
                if (rr, cc) not in opened_reverse:
                # if (rr, cc) not in opened:
                    linksdict[(rr, cc)] = (r, c)
                    #opened[(rr, cc)] = d
                    heapq.heappush(opened, (d, (rr, cc)))
                    costsTo[(rr, cc)] = d
                else:
                    # if opened[(rr, cc)] > d:
                    if opened_reverse[(rr, cc)] > d:
                        linksdict[(rr, cc)] = (r, c)
                        heapq.heappush(opened, (d, (rr, cc)))
                        costsTo[(rr, cc)] = d
        i += 1

    path = []
    curr = end
    while curr != start:
        prev = linksdict[curr]
        path += [curr]
        curr = prev

    pathcost = 0
    for node in path:
        pathcost += input[node[0]][node[1]]
    print("opened", len(linksdict), "nodes in", i, "iterations")
    print("fun took ", tfun)
    return pathcost

def part1(input):
    return dijkstras(input)

def part2(input):
    biggerInput = [[0]*len(input[0])*5 for _ in input*5]
    for r in range(len(input)):
        for c in range(len(input[0])):
            for dr in range(5):
                for dc in range(5):
                    rr = r+dr*len(input)
                    cc = c+dc*len(input[0])
                    v = input[r][c] + dr + dc
                    biggerInput[rr][cc] = v if v < 10 else v-9
    return dijkstras(biggerInput)


stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)