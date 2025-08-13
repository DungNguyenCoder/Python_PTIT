def dao(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

t = int(input())
for _ in range(t):
    n = int(input())
    sum = n
    cnt = 0
    flag = True
    while True:
        if sum % 7 == 0:
            break;
        if cnt >= 1000:
            flag = False
            break
        n1 = dao(n)
        sum = n + n1
        n = sum
    if flag:
        print(sum)
    else:
        print(-1)