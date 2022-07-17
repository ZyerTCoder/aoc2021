

from time import perf_counter as pf

def timer(func):
    N = 100000
    def wrapper(*args, **kwargs):
        t0 = pf()
        for _ in range(N):
            out = func(*args, **kwargs)
        tf = pf()
        print(f"{func.__name__}: " + (f"{out}"))
        print(f"  time: {round(((tf-t0)*1000)/N, 3)} ms")
        return out
    return wrapper

@timer
def solve():
    # x_min = 20
    # x_max = 30
    # y_min = -10
    # y_max = -5

    x_min = 56
    x_max = 76
    y_min = -162
    y_max = -134

    possible_xvels = []
    xvel = 1
    inBounds = False
    done = False
    while not done:
        xpos = (xvel*(xvel+1))//2
        if x_min <= xpos <= x_max:
            inBounds = True
            possible_xvels += [xvel]
        else:
            if inBounds:
                done = True
        xvel += 1

    possible_yvels = []
    yvel = -max(possible_xvels)//2
    inBounds = False
    done = False
    while not done:
        ypos = 0
        done2 = False
        i = 0
        while not done2:
            yvel -= 1
            ypos += yvel
            if y_min <= ypos <= y_max:
                possible_yvels += [-yvel-1]
                done2 = True
            if y_min > ypos:
                done2 = True
                if i == 0:
                    done = True
            i += 1
    possible_starts = []
    for x in possible_xvels:
        for y in possible_yvels:
            possible_starts += [[x, y]]
    maxY = possible_yvels[-1]
    p1 = (maxY*(maxY+1))//2
    
    return p1

solve()