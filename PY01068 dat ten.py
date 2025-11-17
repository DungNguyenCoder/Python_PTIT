from itertools import combinations

n, k = map(int, input().split())
a = input().split()
a = sorted(set(a))
ans = []

for c in combinations(a, k):
    ans.append(' '.join(c))
ans.sort()
for a in ans:
    print(a)