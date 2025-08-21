import math

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if nt(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0
for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()