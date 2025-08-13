t = int(input())

for _ in range(t):
    s = input()
    num1 = s[0]
    num2 = s[1]
    flag = True
    if num1 == num2:
        print("NO")
    else:
        for i in range(2, len(s)):
            if i % 2 == 0 and s[i] != num1:
                flag = False
                break
            elif i % 2 == 1 and s[i] != num2:
                flag = False
                break
    if flag:
        print("YES")
    else:
        print("NO")
# 3
# 12121212
# 343433
# 78789989