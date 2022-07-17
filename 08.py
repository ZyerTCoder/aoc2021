from time import time

INPUT = "inputs/08.txt"

def timer(func, *stuff, n=1):
    t0 = time()
    for i in range(n):
        out = func(*stuff)
    print(f"{func.__name__}: " + (f"{out}" if stuff else ""))
    print(f"  time: {round((((time()-t0)/n)*1000), 3)} ms ave for {n} iteration{'s' if n != 1 else ''}")
    return out

def parser():
    def p(i):
        parts = i.split("|")
        first = [a.strip() for a in parts[0].split()]
        second = [a.strip() for a in parts[1].split()]
        return [first, second]
    with open(INPUT) as f:
        return list(map(p, f.readlines()))

def part1(input):
    o = 0
    for line in input:
        for digit in line[1]:
            if len(digit) in [2, 4, 3, 7]: 
                # number of segments on for 1 4 7 8
                o += 1
    return o

def part2(input):
    out = 0
    for line in input:
        allds = line[0]
        #allds = input[3][0]
        # these will be the code for this particular display
        A, B, C, D, E, F, G = "", "", "", "", "", "", ""
        # these will be the strings on this display that represent the number
        one, two, three, four, five, six, seven, eight, nine, zero = "", "", "", "", "", "", "", "", "", ""
        for digit in allds:
            if len(digit) == 2: # a 1
                one = digit
            if len(digit) == 4: # a 4
                four = digit
            if len(digit) == 3: # a 7
                seven = digit
            if len(digit) == 7: # a 8
                eight = digit
        # top most segment will be on for 7 but not for 1 so
        for l in seven:
            if l not in one:
                A = l
        # the only digits without C and F (one) are 2 5 6 with lengths 5 5 6
        # so the only one that doesnt have CF in them and is length 6 will be the digit 6
        for digit in allds:
            if (one[0] not in digit)^(one[1] not in digit) and len(digit) == 6:
                six = digit
        # so now we can tell which C and F correspond to
        for l in one:
            if l not in six:
                C = l
            if l in six:
                F = l
        # looking at digits of len 5 which are 2 3 5
        is235 = []
        for digit in allds:
            if len(digit) == 5:
                is235.append(digit)
        # only ADG appear in all of them
        ADG = set(is235[0]).intersection(set(is235[1]))
        ADG = ADG.intersection(set(is235[2]))
        # we already know A so remove it
        ADG.remove(A)
        DG = list(ADG)
        # 3 is the only number with ACDFG and we have all of those so
        for d in is235:
            if len(set(d).intersection([A, C, F] + DG)) == 5:
                three = d
        # 0 6 9 are the only 6 digit numbers and 
        for d in allds:
            if len(d) == 6:
                if d == six:
                    continue
                # intersection with 3 will be full for only 9
                if len(set(d).intersection(set(three))) == 5:
                    nine = d
                # intersectoin between 3 and 0 will be 4
                if len(set(d).intersection(set(three))) == 4:
                    zero = d
        # 5 will overlap fully with 6 but 2 wont
        for d in allds:
            if len(d) == 5:
                if len(set(d).intersection(set(six))) == 5:
                    five = d
        for d in is235:
            if (d is not three) and (d is not five):
                two = d
        right = ""
        for digit in line[1]:
        #for digit in input[3][1]:
            if "".join(sorted(one)) == "".join(sorted(digit)): right += "1"
            if "".join(sorted(two)) == "".join(sorted(digit)): right += "2"
            if "".join(sorted(three)) == "".join(sorted(digit)): right += "3"
            if "".join(sorted(four)) == "".join(sorted(digit)): right += "4"
            if "".join(sorted(five)) == "".join(sorted(digit)): right += "5"
            if "".join(sorted(six)) == "".join(sorted(digit)): right += "6"
            if "".join(sorted(seven)) == "".join(sorted(digit)): right += "7"
            if "".join(sorted(eight)) == "".join(sorted(digit)): right += "8"
            if "".join(sorted(nine)) == "".join(sorted(digit)): right += "9"
            if "".join(sorted(zero)) == "".join(sorted(digit)): right += "0"
        #print(right)
        out += int(right)
    return out


stuff = timer(parser)
timer(part1, stuff)
timer(part2, stuff, n=10000)