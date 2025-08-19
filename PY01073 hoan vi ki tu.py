from itertools import permutations

s = input()
for p in permutations(s):
    print("".join(p))