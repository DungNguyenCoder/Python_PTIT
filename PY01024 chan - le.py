def TongChuSo(s):
    sum = 0
    for c in s:
        sum += int(c)
    return sum % 10 == 0

def KTCachNhau(s):
    flag = True
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != 2:
            flag = False
            break
    return flag

t = int(input())
for _ in range(t):
    s = input()
    if TongChuSo(s) and KTCachNhau(s):
        print("YES")
    else:
        print("NO")

