import math

t = int(input())
for _ in range(t):
    s1 = input()
    s2 = s1[::-1]
    flag = True
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
