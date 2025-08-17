t = int(input())
for _ in range(t):
    s = input()
    sumOdd = 0
    mulEven = 1
    flag = False
    for i in range(len(s)):
        if i % 2 == 1:
            sumOdd += int(s[i])
        else:
            if int(s[i]) != 0:
                flag = True
                mulEven *= int(s[i])
    if not flag:
        mulEven = 0
    print(str(mulEven) + " " + str(sumOdd))