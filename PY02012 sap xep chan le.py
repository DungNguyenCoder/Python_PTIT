n = int(input())
a = []
while True:
    tmp = (int(x) for x in input().split())
    a += tmp
    if len(a) == n:
        break

chanle = [0] * n
chan = []
le = []
for i in range(n):
    if a[i] % 2 == 0:
        chanle[i] = 0
        chan.append(a[i])
    else:
        chanle[i] = 1
        le.append(a[i])
chan.sort()
le.sort(reverse=True)

idxChan = 0
idxLe = 0

for i in range(n):
    if chanle[i] == 0:
        print(chan[idxChan], end = " ")
        idxChan += 1
    else:
        print(le[idxLe], end = " ")
        idxLe += 1