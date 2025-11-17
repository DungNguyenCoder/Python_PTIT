n = int(input())
a = list(map(int, input().split()))

b = sorted(a)
med = 0

if n % 2 == 1:
    med = b[n // 2]
else:
    tmp1 = b[n // 2]
    tmp2 = b[n // 2 - 1]
    for x in a:
        if tmp1 == x:
            med = tmp1
            break
        elif tmp2 == x:
            med = tmp2
            break
sum = 0
for x in a:
    sum += abs(x - med)
print(str(sum) + " " + str(med))