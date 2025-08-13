def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

n, k = map(int, input().split())
minK = pow(10, k - 1)
maxK = pow(10, k)
cnt = 0
for i in range(minK, maxK):
    if GCD(i, n) == 1:
        cnt += 1
        if cnt < 10:
            print(str(i), end = " ")
        else:
            print(i)
            cnt = 0

