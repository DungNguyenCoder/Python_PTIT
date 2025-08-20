def checkOut(a, n, x):
    for i in range(n):
        if a[i] != x:
            return False
    return True

while True:
    a = list(map(int, input().split()))
    n = 4
    if checkOut(a, n, 0):
        break
    cnt = 0
    while True:
        if checkOut(a, n, a[0]):
            break
        tmp = a[0]
        for i in range(n - 1):
            a[i] = abs(a[i] - a[i+1])
        a[n - 1] = abs(tmp - a[n - 1])
        cnt += 1
    print(cnt)
