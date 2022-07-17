from time import time
import sys
INPUT = "inputs/9-4096-4.in"
sys.setrecursionlimit(5000)

def timer(func, *stuff, n=1):
    t0 = time()
    for i in range(n):
        out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((((time()-t0)/n)*1000), 3)} ms ave for {n} iteration{'s' if n != 1 else ''}")
    return out

def parser():
    def p(i):
        i = i.strip()
        return [int(c) for c in i]
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def findBasinSize(x, y, grid, checked, level):
    out = 1
    l0 = level
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        xx, yy = x + dx, y + dy
        if 0 <= xx < len(grid) and 0 <= yy < len(grid[1]) and grid[xx][yy] != 9 and checked[xx][yy] == False:
            checked[xx][yy] = True
            s, checked, l = findBasinSize(xx, yy, grid, checked, level + 1)
            l0 = max(l0, l)
            out += s
    return out, checked, l0

def part2(input):
    ans = 1
    checked = [[False]*len(input[0]) for i in range(len(input))]
    basins = []
    d = []
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] == 9:
                checked[x][y] = True
                continue
            if checked[x][y] == False:
                checked[x][y] = True 
                b, checked, l = findBasinSize(x, y, input, checked, 1)
                d.append(l)
                if b:
                    basins.append(b)
    print(max(d))
    for _ in range(3):
        ans *= basins.pop(basins.index(max(basins)))
    return ans


stuff = timer(parser)

timer(part2, stuff)

def visualise(input):
    import cv2
    import numpy
    image = numpy.array(input, 'uint8')
    # for i in range(4096):
    #     for j in range(4096):
    #         if image[i,j] == 9:
    #             image[i,j] = 0
    #         else:
    #             image[i,j] = 200
    #_, image = cv2.threshold(image, 8, 250, cv2.THRESH_BINARY)
    image = numpy.invert(image)
    image = cv2.normalize(image[:2000,:2000], dst=image, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    cv2.imshow("mask", image)
    cv2.waitKey(0)

visualise(stuff)