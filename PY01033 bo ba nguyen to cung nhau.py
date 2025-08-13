import math

l, r = map(int, input().split())
for a in range(l, r - 1):
    for b in range(a + 1, r):
        if math.gcd(a, b) == 1:
            for c in range(b + 1, r + 1):
                if math.gcd(b, c) == 1 and math.gcd(c, a) == 1:
                    print("(" + str(a) + ", " + str(b) + ", " + str(c) + ")")