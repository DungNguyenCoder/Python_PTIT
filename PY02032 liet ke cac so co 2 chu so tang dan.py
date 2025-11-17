s = input()
a = set()
if len(s) % 2 == 1:
    s = s[:-1]
n = len(s)

for i in range(0, n, 2):
    tmp = int(s[i:i + 2])
    a.add(tmp)
a = list(a)
a = sorted(a)
for x in a:
    print(x, end = " ")
