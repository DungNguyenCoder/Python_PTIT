import math


def nt(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num > 1

t = int(input())

for _ in range(t):
    s = input()
    n = sum(int(c) for c in s)
    if nt(n):
        print("YES")
    else:
        print("NO")