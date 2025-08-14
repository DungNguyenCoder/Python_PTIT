t = int(input())

for _ in range(t):
    s = input()
    if len(s) < 3:
        print("NO")
    else:
        flag = False
        for i in range(1, len(s) - 1):
            if s[i - 1] < s[i] and s[i] > s[i + 1]:
                flag = True
                for j in range(1, i):
                    if s[j - 1] >= s[j]:
                        flag = False
                        break
                if flag:
                    for j in range(i + 1, len(s) - 1):
                        if s[j] <= s[j + 1]:
                            flag = False
                            break
        if flag:
            print("YES")
        else:
            print("NO")