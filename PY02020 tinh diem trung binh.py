n = int(input())
a = list(map(float, input().split()))

_max = max(a)
_min = min(a)

avg = 0
cnt = 0

for i in range(n):
    if a[i] != _min and a[i] != _max:
        avg += a[i]
        cnt += 1
ans = avg / cnt
ans = "{:.2f}".format(ans)
print(ans)