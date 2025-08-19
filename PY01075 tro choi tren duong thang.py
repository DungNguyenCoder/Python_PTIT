import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dp = {0 : 0}
    for i in range(n):
        ai, ci = a[i], c[i]
        newDp = dp.copy()
        for g, cost in dp.items():
            newG = math.gcd(g, ai)
            newCost = cost + ci
            if newG not in newDp or newCost < newDp[newG]:
                newDp[newG] = newCost
        dp = newDp
    print(dp[1] if 1 in dp else -1)