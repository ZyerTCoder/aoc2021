f = open("inputs/01.txt")

def parser(file):
    return [int(i) for i in file.read().strip().split("\n")]

def part1(input):
    o = 0
    for i in range(1, len(input)):
        if input[i] > input[i-1]:
            o += 1
    return o

def part2(input):
    o = 0
    for i in range(2, len(input)-1):
        if input[i+1] > input[i-2]:
            o += 1
    return o

stuff = parser(f)
print(part1(stuff))
print(part2(stuff))