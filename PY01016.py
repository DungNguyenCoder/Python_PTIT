t = int(input())
for _ in range(t):
    s = input()
    for i in range(len(s)):
        cnt = 0
        if s[i].isdigit():
            cnt = int(s[i])
            while cnt > 0:
                print(s[i - 1], end = "")
                cnt -= 1
    print()