s1 = input().lower()
s2 = input().lower()

a = set(s1.split())
b = set(s2.split())

giao = sorted(list(a & b))
hop = sorted(list(a | b))

for i in hop:
    print(i, end=' ')
print()
for i in giao:
    print(i, end=' ')
