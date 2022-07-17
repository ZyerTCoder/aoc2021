from time import time
from math import log2, ceil, prod

INPUT = "inputs/16.txt"

def timer(func, *stuff):
    t0 = time()
    out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ":"))
    print(f"  time: {round((time()-t0)*1000, 3)} ms")
    return out

def parser():
    with open(INPUT) as f:
        hex = f.read().strip()
        pad =  "0"*(4 - ceil(log2(int(hex[0], 16)+1)))
        return pad + format(int(hex, 16), "b")

def decode_x(b, p, x):
    return int(b[p:p+x], 2), p+x

def decode_id4(b, p):
    out = ""
    done = False
    while not done:
        if b[p] == "0":
            done = True
        out += b[p+1:p+5]
        p += 5
    return int(out, 2), p

def decode_packet(input, p):
    version, p = decode_x(input, p, 3)
    id, p = decode_x(input, p, 3)
    #print("= vers:", version, "id:",id)
    if id == 4:
        literal, p = decode_id4(input, p)
        return version, id, "l", literal, p
    mode, p = decode_x(input, p, 1)
    if mode == 0:
        length, p = decode_x(input, p, 15)
        return version, id, "a", length, p
    else:
        num, p = decode_x(input, p, 11)
        return version, id, "p", num, p

D = {0: "sum", 1: "prod", 2:"min", 3:"max", 4:"lit", 5:"great", 6:"less", 7:"equal"}

def part1(input):
    #print(input)
    p = 0
    packets = [["b"]]
    version_total = 0
    literals = []
    while len(packets):
        #print("packets ", packets)
        #print(".".join([input[p:p+3],input[p+3:p+6],input[p+6:p+7],input[p+7:p+22]]))
        if packets[-1][0] == "b":
            vers, id, typ, out, p = decode_packet(input,p)
            literals.append(D[id])
            packets.pop(-1)
        elif packets[-1][0] == "a":
            if packets[-1][1] > p:
                vers, id, typ, out, p = decode_packet(input,p)
                literals.append(D[id])
            else:
                packets.pop(-1)
                continue
        elif packets[-1][0] == "p":
            packets[-1][1] -= 1 
            vers, id, typ, out, p = decode_packet(input,p)
            literals.append(D[id])
            if packets[-1][1] == 0:
                packets.pop(-1)
        elif packets[-1][0] == "l":
            literals += [packets[-1][1]]
            packets.pop(-1)
            continue

        if typ == "a":
            out += p
        packets.append([typ, out])
        version_total += vers
    #print(literals)
    return version_total

def calcop(nums):
    op = nums.pop(0)
    match op:
        case "sum":
            return sum(nums)
        case "prod":
            return prod(nums)
        case "min":
            return min(nums)
        case "max":
            return max(nums)
        case "great":
            return nums[0] > nums[1]
        case "less":
            return nums[0] < nums[1]
        case "equal":
            return nums[0] == nums[1]
    print("wtf")
    return False

def part2(input):
    p = 0
    packets = [["b"]]
    operands = []
    while len(packets):
        #print("packets ", packets)
        #print(".".join([input[p:p+3],input[p+3:p+6],input[p+6:p+7],input[p+7:p+22]]))
        if packets[-1][0] == "b":
            vers, id, typ, out, p = decode_packet(input,p)
            packets.pop(-1)
        elif packets[-1][0] == "a":
            if packets[-1][1] > p:
                vers, id, typ, out, p = decode_packet(input,p)
            else:
                tmp = packets.pop(-1)
                res = calcop(tmp[2])
                if len(packets):
                    packets[-1][2].append(res)
                else:
                    return res
                continue
        elif packets[-1][0] == "p":
            if packets[-1][1] > 0:
                packets[-1][1] -= 1 
                vers, id, typ, out, p = decode_packet(input,p)
            else:
                tmp = packets.pop(-1)
                res = calcop(tmp[2])
                if len(packets):
                    packets[-1][2].append(res)
                else:
                    return res
                continue
        elif packets[-1][0] == "l":
            packets[-2][2].append(packets[-1][1])
            packets.pop(-1)
            continue

        if typ == "a":
            out += p
        packets.append([typ, out, [D[id]]])
    #print(literals)
    return operands


stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)