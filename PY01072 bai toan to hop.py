from itertools import combinations

n, k = map(int, input().split())
a = list(map(int, input().split()))

union = sorted(set(a))
for c in combinations(union, k):
    for i in c:
        print(i, end = " ")
    print()
