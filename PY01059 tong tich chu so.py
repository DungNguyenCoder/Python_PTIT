t = int(input())
for _ in range(t):
    s = input()
    sumEven = 0
    mulOdd = 1
    flag = False
    for i in range(len(s)):
        if i % 2 == 0:
            sumEven += int(s[i])
        else:
            if int(s[i]) != 0:
                flag = True
                mulOdd *= int(s[i])
    if not flag:
        mulOdd = 0
    print(str(sumEven) + " " + str(mulOdd))