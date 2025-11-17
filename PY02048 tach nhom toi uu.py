n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

group = []
tmp = []

for i in range(n):
    if not tmp:
        tmp.append(a[i])
    else:
        if a[i] - tmp[-1] <= k:
            tmp.append(a[i])
        else:
            group.append(tmp)
            tmp = [a[i]]
if tmp:
    group.append(tmp)

print(len(group))

# 1 2 3 4 6 7 9

