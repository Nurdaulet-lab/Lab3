def solve(numheads, numlegs):
    c = (4 * numheads - numlegs) // 2
    r = numheads - c
    print(c, r)

numheads = 35
numlegs = 94

solve(numheads, numlegs)
