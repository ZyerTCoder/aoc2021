from time import time
from math import log2, ceil

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
    print("=== vers:", version, "id:",id)
    if id == 4:
        literal, p = decode_id4(input, p)
        #p += 4-p%4 # finish out the id 4 header
        #print(input[p:])
        return version, ["l", literal], p
        #print(num, end=" ")

    mode, p = decode_x(input, p, 1)
    if mode == 0:
        length, p = decode_x(input, p, 15)
        print("=== mode:", mode, "with ", length, "bits of packets inside")
        packets = input[p:p+length]
        return version, [["a", packets, length]], p+length
    else:
        num, p = decode_x(input, p, 11)
        print("=== mode:", mode, "with", num, "packets inside")
        packet = input[p:]
        out = [["p", packet, num]]
        return version, out, len(input)

def part1(input):
    p = 0
    packets = [["b", input]]
    version_total = 0
    literals = []
    while len(packets):
        print("packets left", packets)
        p = 0
        packet = packets.pop(0)
        #print("=looking at", packet)
        if packet[0] == "b":
            vers, out, p = decode_packet(packet[1], 0)
        elif packet[0] == "p":
            vers, out, p = decode_packet(packet[1], 0)
            packet[2] -= 1
            if out[0][0] == "p":
                out[0][2] += packet[2]
            elif packet[2] > 0:
                packet[1] = packet[1][p:]
                packets += [packet]
        elif packet[0] == "a":
            vers, out, p = decode_packet(packet[1], 0)
            if packet[2] > p:
                packet[1] = packet[1][p:]
                packet[2] = packet[2] - p
                packets += [packet]
        version_total += vers
        print("=out", out)

        if out[0][0] == "p" or out[0][0] == "a":
            packets += out
        elif out[0][0] == "l":
            literals += [out[1]]
    print("done")
    print(literals)
    return version_total

def part2(input):
    return


stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff)