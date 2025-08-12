cal = input().strip()

a, plus, b, eq, c = cal.split()

a = int(a)
b = int(b)
c = int(c)

if a + b == c:
    print("YES")
else:
    print("NO")