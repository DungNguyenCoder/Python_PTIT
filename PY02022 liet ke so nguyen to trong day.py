import math


def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

a = list(map(int, input().split()))
mp = {}

for i in range(n):
    mp[a[i]] = mp.get(a[i], 0) + 1

for i in range(n):
    if mp[a[i]] != 0 and nt(a[i]):
        print(str(a[i]) + " " + str(mp[a[i]]))
        mp[a[i]] = 0
