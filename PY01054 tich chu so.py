t = int(input())
for _ in range(t):
    n = int(input())
    sum = 1
    while n > 0:
        a = n % 10
        if a != 0:
            sum *= a
        n //= 10
    print(sum)