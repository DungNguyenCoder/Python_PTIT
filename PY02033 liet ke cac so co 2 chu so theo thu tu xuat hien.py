s = input()
a = set()
b = []
if len(s) % 2 == 1:
    s = s[:-1]
n = len(s)

for i in range(0, n, 2):
    tmp = int(s[i:i + 2])
    if tmp not in a:
        a.add(tmp)
        b.append(tmp)

for x in b:
    print(x, end = " ")
