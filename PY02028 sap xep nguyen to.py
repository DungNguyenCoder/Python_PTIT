import math


def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

# main
n = int(input())
a = list(map(int, input().split()))
b = []
check_point = [0] * n

for i in range(n):
    if nt(a[i]):
        b.append(a[i])
        check_point[i] = 1
    else:
        check_point[i] = 0
b.sort()
idx = 0
for i in range(n):
    if check_point[i] == 1:
        print(b[idx], end=' ')
        idx += 1
    else:
        print(a[i], end=' ')


