from time import time
import numpy as np
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
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
        paper = [[255]*(maxCol+1) for _ in range(maxRow+1)]
        for dot in dots:
            paper[dot[1]][dot[0]] = 0
        instructions = [i[11:].strip() for i in instructions.split("\n")]
        return paper, instructions
        
def part1(paper, instructions):
    if instructions[0][0] == "y":
        fold = int(instructions[0][2:])
        for row in range(fold, len(paper)):
            for col in range(len(paper[0])):
                if paper[row][col] == 0:
                    paper[len(paper)-row-1][col] = 0
        paper = paper[0:fold]
    else:
        fold = int(instructions[0][2:])
        for row in range(len(paper)):
            for col in range(fold, len(paper[0])):
                if paper[row][col] == 0:
                    paper[row][len(paper[0])-col-1] = 0
        paper = [row[0:fold] for row in paper]
    dots = 0
    for row in paper:
        dots += row.count(0)
    return dots

def part2(paper, instructions):
    for instruction in instructions:
        if instruction[0] == "y":
            fold = int(instruction[2:])
            for row in range(fold, len(paper)):
                for col in range(len(paper[0])):
                    if paper[row][col] == 0:
                        paper[len(paper)-row-1][col] = 0
            paper = paper[0:fold]
        else:
            fold = int(instruction[2:])
            for row in range(len(paper)):
                for col in range(fold, len(paper[0])):
                    if paper[row][col] == 0:
                        paper[row][len(paper[0])-col-1] = 0
            paper = [row[0:fold] for row in paper]
    
    image = np.array(paper, 'uint8')
    image = cv2.resize(image, None, fx = 2, fy = 2, interpolation=cv2.INTER_CUBIC)
    image = cv2.copyMakeBorder(image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, None, 255)
    # cv2.imshow("asd", image)
    # cv2.waitKey(0)
    text = pytesseract.image_to_string(image)
    return text.replace(" ", "").strip()


paper, instructions = timer(parser)
timer(part1, paper, instructions)
timer(part2, paper, instructions)