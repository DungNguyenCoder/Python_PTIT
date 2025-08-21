def DigitSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(key = lambda x : (DigitSum(x), x))

    for i in a:
        print(i, end = " ")
    print()