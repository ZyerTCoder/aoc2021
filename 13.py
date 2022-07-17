from time import time

INPUT = "inputs/13.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    def p(i):
        return i
    with open(INPUT) as f:
        dots, instructions = f.read().split("\n\n")
        dots = [[int(i) for i in l.split(",")] for l in dots.split("\n")]
        maxRow = maxCol = 0
        for dot in dots:
            if dot[0] > maxCol:
                maxCol = dot[0]
            if dot[1] > maxRow:
                maxRow = dot[1]
        paper = [["."]*(maxCol+1) for _ in range(maxRow+1)]
        for dot in dots:
            paper[dot[1]][dot[0]] = "#"
        instructions = [i[11:].strip() for i in instructions.split("\n")]
        return paper, instructions
        
def part1(paper, instructions):
    if instructions[0][0] == "y":
        fold = int(instructions[0][2:])
        for row in range(fold, len(paper)):
            for col in range(len(paper[0])):
                if paper[row][col] == "#":
                    paper[len(paper)-row-1][col] = "#"
        paper = paper[0:fold]
    else:
        fold = int(instructions[0][2:])
        for row in range(len(paper)):
            for col in range(fold, len(paper[0])):
                if paper[row][col] == "#":
                    paper[row][len(paper[0])-col-1] = "#"
        paper = [row[0:fold] for row in paper]
    dots = 0
    for row in paper:
        dots += row.count("#")
    return dots

def part2(paper, instructions):
    for instruction in instructions:
        if instruction[0] == "y":
            fold = int(instruction[2:])
            for row in range(fold, len(paper)):
                for col in range(len(paper[0])):
                    if paper[row][col] == "#":
                        paper[len(paper)-row-1][col] = "#"
            paper = paper[0:fold]
        else:
            fold = int(instruction[2:])
            for row in range(len(paper)):
                for col in range(fold, len(paper[0])):
                    if paper[row][col] == "#":
                        paper[row][len(paper[0])-col-1] = "#"
            paper = [row[0:fold] for row in paper]
    for line in paper:
        print("".join(line))
    return


paper, instructions = timer(parser)
timer(part1, paper, instructions)
timer(part2, paper, instructions)