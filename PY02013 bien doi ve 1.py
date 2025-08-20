while True:
    n = int(input())
    if n == 0:
        break
    a = []
    while True:
        a.append(n)
        if n == 1:
            break
        elif n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1
    print(len(a))

