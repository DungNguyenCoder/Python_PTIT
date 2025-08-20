n = int(input())
a = list(map(int, input().split()))
cnt = 0
for u in range(n - 1):
    for v in range(u + 1, n):
        if a[u] > a[v]:
            cnt += 1
print(cnt)