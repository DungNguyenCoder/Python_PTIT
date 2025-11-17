t = int(input())

for _ in range(t):
    n, m, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    i = j = k = 0
    res = []

    while i < n and j < m and k < p:
        if a[i] == b[j] == c[k]:
            res.append(a[i])
            i += 1
            j += 1
            k += 1
        else:
            mn = min(a[i], b[j], c[k])
            if a[i] == mn:
                i += 1
            elif b[j] == mn:
                j += 1
            else:
                k += 1
    if res:
        for i in res:
            print(i, end=' ')
        print()
    else:
        print("NO")
