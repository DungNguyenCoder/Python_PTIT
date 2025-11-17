t = int(input())
for _ in range(t):
    s = input()
    r = input()
    n = len(s)
    m = len(r)
    cnt = 0
    i = 0
    while i <= n - m:
            tmp = s[i : i + m]
            if tmp == r:
                cnt += 1
                i += m
            else:
                i += 1
    print(cnt)