import math

def tn(n):
    if n < 10:
        return False
    tmp = n
    rev = 0
    while tmp != 0:
        rev = rev * 10 + tmp % 10
        tmp //= 10
    return n == rev

#main
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

maxNt = 0
for i in range(n):
    for j in range(m):
        if tn(a[i][j]):
            maxNt = max(maxNt, a[i][j])
if maxNt != 0:
    print(maxNt)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxNt:
                print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")
# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77
