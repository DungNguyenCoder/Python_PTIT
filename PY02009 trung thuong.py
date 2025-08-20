t = int(input())
for _ in range(t):
    n = int(input())
    mp = {}
    for i in range(n):
        x = int(input())
        mp[x] = mp.get(x, 0) + 1
    maxx = max(mp.values())
    a = []
    for k, v in mp.items():
        # print(k, v)
        if v == maxx:
            a.append(k)
    a.sort()
    print(a[0])
