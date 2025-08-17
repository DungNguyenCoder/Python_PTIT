import math


def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
for _ in range(t):
    s = input()
    first = int(s[:3])
    last = int(s[-3:])
    if nt(first) and nt(last):
        print("YES")
    else:
        print("NO")
