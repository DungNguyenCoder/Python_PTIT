import math

mx = 1000000
nt = [1] * (mx + 5)
prime = []

def sang():
    nt[0] = 0
    nt[1] = 0
    for i in range(2, int(math.sqrt(mx)) + 1):
        if nt[i]:
            for j in range(i * i, mx + 1, i):
                nt[j] = 0
    for i in range(2, mx + 1):
        if nt[i]:
            prime.append(i)

sang()
n, x = map(int, input().split())
idx = 0
while idx <= n:
    print(x, end = " ")
    x += prime[idx]
    idx += 1

