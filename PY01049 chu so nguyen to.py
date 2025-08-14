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
            a = ord(c) - ord('0')
            if a == 2 or a == 3 or a == 5 or a == 7:
                cntNt += 1
        if cntNt > len(s) // 2:
            print("YES")
        else:
            print("NO")