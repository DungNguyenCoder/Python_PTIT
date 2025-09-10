n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
sumUp = 0
sumDown = 0

for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            sumUp += a[i][j]
        if j > n - i - 1:
            sumDown += a[i][j]
sum = abs(sumUp - sumDown)
if sum <= k:
    print("YES")
else:
    print("NO")
print(sum)

