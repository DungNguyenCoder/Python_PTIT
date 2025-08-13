t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0
    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            ans += 1/i
    else:
        for i in range(2, n + 1, 2):
            ans += 1/i
    print(f"{ans:.6f}")