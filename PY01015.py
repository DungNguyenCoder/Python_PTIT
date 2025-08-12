t = int(input())

for _ in range(t):
    s = input()
    flag = True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")