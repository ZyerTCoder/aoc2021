INPUT = "inputs/13.txt"

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
        paper = [[0]*(maxCol+1) for _ in range(maxRow+1)]
        for dot in dots:
            paper[dot[1]][dot[0]] = 255
        instructions = [i[11:].strip() for i in instructions.split("\n")]
        return paper, instructions
        
def ocr(image):
    import numpy as np
    import cv2
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image = np.array(image, 'uint8')
    image = cv2.resize(image, None, fx = 2, fy = 2, interpolation=cv2.INTER_CUBIC)
    image = cv2.copyMakeBorder(image, 5, 5, 5, 5, cv2.BORDER_CONSTANT)
    text = pytesseract.image_to_string(image)
    return text.replace(" ", "").strip()

def main(paper, instructions):
    for instruction in instructions:
        if instruction[0] == "y":
            fold = int(instruction[2:])
            for row in range(fold, len(paper)):
                for col in range(len(paper[0])):
                    if paper[row][col]:
                        paper[len(paper)-row-1][col] = 255
            paper = paper[0:fold]
        else:
            fold = int(instruction[2:])
            for row in range(len(paper)):
                for col in range(fold, len(paper[0])):
                    if paper[row][col]:
                        paper[row][len(paper[0])-col-1] = 255
            paper = [row[0:fold] for row in paper]
        if instruction == instructions[0]:
            dots = 0
            for row in paper:
                dots += row.count(255)
    print(f"part1: {dots}\npart2: {ocr(paper)}")
    return


paper, instructions = parser()
main(paper, instructions)
