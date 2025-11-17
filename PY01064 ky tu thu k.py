def find_char(n, k):
    if n == 1:
        return 'A'
    mid = 1 << (n - 1)
    if k == mid:
        return chr(ord('A') + n - 1)
    elif k < mid:
        return find_char(n - 1, k)
    else:
        return find_char(n - 1, k - mid)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_char(n, k))
