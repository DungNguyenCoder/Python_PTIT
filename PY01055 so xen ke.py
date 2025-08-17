def check(s):
    cntDigit = 0
    if(len(s) == 1):
        return True
    if(s[0] == s[1]):
        return False
    for i in range(2, len(s), 2):
        if(s[i] != s[i - 2]):
            return False
    if s[0] != s[len(s) - 1]:
        return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")