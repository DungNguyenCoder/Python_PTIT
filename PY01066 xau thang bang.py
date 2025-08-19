t = int(input())
for _ in range(t):
    s = input()
    l = 0
    r = len(s) - 1
    flag = True
    while l < r:
        if abs(ord(s[l]) - ord(s[l + 1])) != abs(ord(s[r]) - ord(s[r - 1])):
            flag = False
            break
        l += 1
        r -= 1
    if flag:
        print("YES")
    else:
        print("NO")