def tn(n):
    s = 0
    for i in n:
        s += int(i)
    if s == int(str(s)[::-1]) and s > 10:
        return True
    return False

t = int(input())

for _ in range(t):
    n = input()
    if tn(n):
        print("YES")
    else:
        print("NO")