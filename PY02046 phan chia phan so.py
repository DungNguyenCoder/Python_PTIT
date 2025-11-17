import math


def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))
seen = set()
a = []
for x in arr:
    if x not in seen:
        a.append(x)
        seen.add(x)
n = len(a)
b = [0] * n
b[0] = a[0]
for i in range(1, n):
    b[i] = a[i] + b[i-1]
flag = False
for i in range(n - 1):
    if nt(b[i]) and nt(b[n-1] - b[i]):
        print(i)
        flag = True
        break
if not flag:
    print("NOT FOUND")
