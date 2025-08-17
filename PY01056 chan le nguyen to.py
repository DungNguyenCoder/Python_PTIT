import math

def nt(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num > 1

def check(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
        if (i % 2 == 0 and int(s[i]) % 2 == 1) or (i % 2 == 1 and int(s[i]) % 2 == 0):
            return False
    return nt(sum)

t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")