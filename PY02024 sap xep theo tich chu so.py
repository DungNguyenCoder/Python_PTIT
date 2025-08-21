def DigitMul(n):
    mul = 1
    while n > 0:
        mul *= n % 10
        n = n // 10
    return mul

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(key = lambda x : (DigitMul(x), x))

    for i in a:
        print(i, end = " ")
    print()