#main
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

maxx = 0
minn = 10005
for i in range(n):
    for j in range(m):
        maxx = max(maxx, a[i][j])
        minn = min(minn, a[i][j])
soMayMan = maxx - minn
flag = False
for i in range(n):
    for j in range(m):
        if a[i][j] == soMayMan:
            flag = True
            break
if flag:
    print(soMayMan)
    for i in range(n):
        for j in range(m):
            if a[i][j] == soMayMan:
                print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")
# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77