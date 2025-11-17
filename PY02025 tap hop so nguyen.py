n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = list(a & b)
d = list(a - b)
e = list(b - a)

c.sort()
d.sort()
e.sort()

for x in c:
    print(x, end=' ')
print()
for x in d:
    print(x, end=' ')
print()
for x in e:
    print(x, end=' ')