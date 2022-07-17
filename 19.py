from time import perf_counter as pf

INPUT = "inputs/1.txt"

def timer(func):
    N = 100000
    def wrapper(*args, **kwargs):
        t0 = pf()
        for _ in range(N):
            out = func(*args, **kwargs)
        tf = pf()
        print(f"{func.__name__}: " + (f"{out}" if len(stuff) else ""))
        print(f"  time: {round(((tf-t0)*1000)/N, 3)} ms")
        return out
    return wrapper

@timer
def parser():
    with open(INPUT) as f:
        scanners = f.read().split("\n\n")

@timer
def part1(input):
    return

@timer
def part2(input):
    return


stuff = parser()
part1(stuff)
part2(stuff)