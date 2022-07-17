INPUT = "inputs/13.txt"
BG = "  "
DOT = "▮▮"

def parser():
    with open(INPUT) as f:
        dots, instructions = f.read().split("\n\n")
        dots = [[int(i) for i in l.split(",")] for l in dots.split("\n")]
        maxRow = maxCol = 0
        for dot in dots:
            if dot[0] > maxCol:
                maxCol = dot[0]
            if dot[1] > maxRow:
                maxRow = dot[1]
        paper = [[BG]*(maxCol+1) for _ in range(maxRow+1)]
        for dot in dots:
            paper[dot[1]][dot[0]] = DOT
        instructions = [i[11:].strip() for i in instructions.split("\n")]
        return paper, instructions

def main(paper, instructions):
    for instruction in instructions:
        fold = int(instruction[2:])
        if instruction[0] == "y":
            for row in range(fold, len(paper)):
                for col in range(len(paper[0])):
                    if paper[row][col] == DOT:
                        paper[len(paper)-row-1][col] = DOT
            paper = paper[0:fold]
        else:
            for row in range(len(paper)):
                for col in range(fold, len(paper[0])):
                    if paper[row][col] == DOT:
                        paper[row][len(paper[0])-col-1] = DOT
            paper = [row[0:fold] for row in paper]
        if instruction == instructions[0]:
            dots = 0
            for row in paper:
                dots += row.count(DOT)
    print(f"part1: {dots}")
    print(f"part2:")
    for line in paper:
        print("".join(line))
    return


paper, instructions = parser()
main(paper, instructions)
