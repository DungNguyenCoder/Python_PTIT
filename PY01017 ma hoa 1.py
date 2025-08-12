t = int(input())
for _ in range(t):
    s = input()
    s += '@'
    cnt = 0
    for i in range(1, len(s)):
        cnt += 1
        if s[i] != s[i - 1]:
            print(str(cnt) + s[i - 1], end = "")
            cnt = 0
    print()