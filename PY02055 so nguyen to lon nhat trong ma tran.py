import math

def nt(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1

#main
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

maxNt = 0
for i in range(n):
    for j in range(m):
        if nt(a[i][j]) == True:
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
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29
