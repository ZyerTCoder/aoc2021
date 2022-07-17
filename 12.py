from time import time
import string
import sys
#sys.setrecursionlimit(5000)

INPUT = "inputs/12.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parserFull():
    def p(i):
        return i.strip().split("-")
    with open(INPUT) as f:
        connections = list(map(p, f.readlines()))
        flatl = [i for sub in connections for i in sub]
        nodesList = []
        for i in flatl:
            if i not in nodesList:
                nodesList.append(i)
        nodesDict = {}
        for node in nodesList:
            nodesDict[node] = []
            for connection in connections:
                if node in connection:
                    nodesDict[node] += [connection[1-connection.index(node)]]   
        return nodesDict

def parser():
    def p(i):
        return i.strip().split("-")
    with open(INPUT) as f:
        connections = list(map(p, f.readlines()))
        flatl = [i for sub in connections for i in sub]
        nodesList = []
        for i in flatl:
            if i not in nodesList:
                nodesList.append(i)
        nodesDict = {}
        for node in nodesList:
            if node == "end": continue
            nodesDict[node] = []
            for connection in connections:
                if node in connection:
                    link = connection[1-connection.index(node)]
                    if link != "start":
                        nodesDict[node] += [link] 
            #print(node, nodesDict[node])  
        return nodesDict

PATHS = []

def traverse(map, start="start", path=["start"]):
    for node in map[start]:
        if node == "end":
            global PATHS
            PATHS += [path+["end"]]
            #print(",".join(PATHS[-1]))
            continue
        if node.islower() and node in path:
            continue
        traverse(map, node, path+[node])
    return 

def part1(map):
    traverse(map)
    return len(PATHS)

PATHS2 = []

def canDupe(map, path):
    lowerOccurs = {}
    for node in map:
        if node.islower():
            if path.count(node) > 1:
                return True
    return False
            #lowerOccurs[node] = path.count(node)

def traverse2(map, start="start", path=["start"]):
    for node in map[start]:
        if node == "end":
            global PATHS2
            PATHS2 += [path+["end"]]
            #print(",".join(PATHS2[-1]))
            continue
        if node.islower() and node in path:
            if canDupe(map, path):
                continue
        traverse2(map, node, path+[node])
    return 

def part2(map):
    traverse2(map)
    return len(PATHS2)


stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)