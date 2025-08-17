import math


def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if not nt(n):
        print("NO")
    else:
        cntNt = 0
        for c in s:
            if nt(int(c)):
                cntNt += 1
        cntKnt = n - cntNt
        if cntNt > cntKnt:
            print("YES")
        else:
            print("NO")