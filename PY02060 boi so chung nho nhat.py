import math
import sys

MOD = 10**9 + 7
mx = 1000000
prime = [0] * (mx + 5)


def sang():
    for i in range(1, mx + 1):
        prime[i] = i;
    for i in range(2, int(math.sqrt(mx)) + 1):
        if prime[i]:
            for j in range(i * i, mx + 1, i):
                if prime[j] == j:
                    prime[j] = i

def pt(mp, n):
    while n != 1:
        cnt = 0
        tmp = prime[n]
        while n % tmp == 0:
            cnt += 1
            n //= tmp
        mp[tmp] = mp.get(tmp, 0) + cnt


sang()

data = sys.stdin.read().split()
it = iter(data)
t = int(next(it))
for _ in range(t):
    a = int(next(it)); b = int(next(it))
    mp = {}
    for x in range(a, b + 1):
        pt(mp, x)
    ans = 1
    for k, v in mp.items():
        ans = (ans * (2 * v + 1)) % MOD
    print(ans)
