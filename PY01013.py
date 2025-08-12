import math

def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

def nt(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    GCD = ucln(a, b)
    sum = 0
    while GCD > 0:
        sum += GCD % 10
        GCD //= 10
    if nt(sum):
        print("YES")
    else:
        print("NO")
