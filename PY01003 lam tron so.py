T = int(input())

for _ in range(T):
    n = int(input())
    m = 10
    while n >= m:
        rem = n % m
        if rem >= m / 2:
            n = n - rem + m
        else:
            n = n - rem
        m *= 10
    print(n)