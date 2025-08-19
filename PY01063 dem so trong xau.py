t = int(input())

for _ in range(t):
    s = input()
    n = input()
    cnt = 0
    i = 0
    while i <= len(s) - len(n):
        sub = s[i : i + len(n)]
        if sub == n:
            cnt += 1
            i += len(n)
        else:
            i += 1
    print(cnt)
