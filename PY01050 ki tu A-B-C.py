from itertools import product

n = int(input())

res = []

def backtrack(s, cntA, cntB, cntC):
    if len(s) >= 3 and cntA > 0 and cntB > 0 and cntC > 0:
        if cntA <= cntB <= cntC:
            res.append(s)
    if len(s) == n:
        return

    backtrack(s + 'A', cntA + 1, cntB, cntC)
    backtrack(s + 'B', cntA, cntB + 1, cntC)
    backtrack(s + 'C', cntA, cntB, cntC + 1)

backtrack("",0 , 0, 0)

res.sort(key = lambda x : (len(x),x))

for s in res:
    print(s)