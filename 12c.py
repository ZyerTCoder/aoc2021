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
        return nodesDict

PATHS = []
PATHS2 = []

def canDupe(map, path):
    for node in map:
        if node.islower():
            if path.count(node) > 1:
                return True
    return False

def traverse(map, start="start", path=["start"], part2=False):
    for node in map[start]:
        if node == "end":
            if part2:
                global PATHS2
                PATHS2 += [path+["end"]]
            else:
                global PATHS
                PATHS += [path+["end"]]
            continue
        if node.islower() and node in path:
            if not part2 or canDupe(map, path):
                continue
        traverse(map, node, path+[node], part2)
    return 

stuff = parser()
traverse(stuff)
traverse(stuff, part2=True)
print(len(PATHS), len(PATHS2))