t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    for k, v in freq.items():
        if v % 2 == 1:
            print(k)
            break
