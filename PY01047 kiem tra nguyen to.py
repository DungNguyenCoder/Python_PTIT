import math


def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())

for _ in range(t):
    s = input()
    last = int(s[-4:])
    if nt(last):
        print("YES")
    else:
        print("NO")
