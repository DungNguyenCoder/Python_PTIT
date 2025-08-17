import math


def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

a = [2, 3, 5, 7]

t = int(input())
for _ in range(t):
    s = input()
    flag = True
    for i in range(len(s)):
        for j in range(len(a)):
            if int(s[i]) == a[j] and (not nt(i)):
                print("NO")
                flag = False
                break
        if not flag:
            break
    if flag:
        print("YES")
