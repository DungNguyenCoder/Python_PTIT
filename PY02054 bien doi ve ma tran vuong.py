n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))
if n > m:
    dis = n - m
    for i in range(n):
        if i % 2 == 0 and dis != 0:
            dis -= 1
        else:
            for j in range(m):
                print(a[i][j], end=" ")
            print()
elif n < m:
    for i in range(n):
        dis = m - n
        for j in range(m):
            if j % 2 == 1 and dis != 0:
                dis -= 1
            else:
                print(a[i][j], end=" ")
        print()
else:
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=" ")
        print()
# 6 4
# 2 8 7 6
# 6 3 2 6
# 7 2 2 8
# 9 9 9 8
# 9 6 6 3
# 7 7 4 9

# 4 6
# 2 8 7 6 4 3
# 6 3 2 6 7 2
# 7 2 2 8 9 1
# 9 9 9 8 0 7