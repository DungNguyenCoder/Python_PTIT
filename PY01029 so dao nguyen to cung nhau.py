def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

t = int(input())

for _ in range(t):
    s = input()
    n = int(s)
    n1 = int(s[::-1])
    if GCD(n, n1) != 1:
        print("NO")
    else:
        print("YES")