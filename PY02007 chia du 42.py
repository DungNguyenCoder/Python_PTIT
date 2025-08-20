import sys

a = list(map(int, sys.stdin.read().split()))
n = len(a)
for i in range(n):
    a[i] = a[i] % 42
b = set(a)
print(len(b))