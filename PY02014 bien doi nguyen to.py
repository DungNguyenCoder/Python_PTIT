import math

nt = [1] * 20005

def sang():
    nt[0] = 0
    nt[1] = 0
    for i in range(2, int(math.sqrt(20000)) + 1):
        if nt[i] == 1:
            for j in range(i * i, 20001, i):
                nt[j] = 0

sang()
n = int(input())
a = list(map(int, input().split()))

sum = 0
ntUp = 0
ntDown = 0

for i in range(n):
    if a[i] == 0:
        sum = max(sum, 2)
    elif a[i] == 1:
        sum = min(sum, 1)
    elif nt[a[i]] != 1:
        tmp1 = a[i]
        while True:
            tmp1 -= 1
            if nt[tmp1] == 1:
                ntDown = tmp1
                break
        tmp1 = a[i]
        while True:
            tmp1 += 1
            if nt[tmp1] == 1:
                ntUp = tmp1
                break
        sum = max(sum, min(abs(ntUp - a[i]), abs(ntDown - a[i])))
print(sum)
