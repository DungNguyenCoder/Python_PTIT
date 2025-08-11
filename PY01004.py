import math

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def phi(n):
    res = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res = res - res//i
            while n % i == 0:
                n //= i
    if n > 1:
        res = res - res//n
    return res

t = int(input())

for _ in range(t):
    n = int(input())
    if nt(phi(n)) == True:
        print("YES")
    else:
        print("NO")