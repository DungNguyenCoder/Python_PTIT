import math

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, int(math.sqrt(n)) + 1):
        cnt = 0
        if n % i == 0:
            if i == 1:
                print(i, end = " ")
            else:
                while n % i == 0:
                    cnt += 1
                    n //= i
                print(str(i) + "^" + str(cnt), end = " ")
            if n != 1:
                print("*", end = " ")
    if n != 1:
        print(str(n) + "^" + str(1), end = " ")
    print()
