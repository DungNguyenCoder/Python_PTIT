t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mp = {}
    for i in range(n):
        mp[a[i]] = mp.get(a[i], 0) + 1
    flag = False
    for k, v in mp.items():
        if v > n//2:
            print(k)
            flag = True
    if not flag:
        print("NO")

