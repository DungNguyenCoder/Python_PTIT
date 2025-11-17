while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for _ in range(n):
        a.append(int(input()))
    minn = min(a)
    maxx = max(a)
    if minn == maxx:
        print("BANG NHAU")
    else:
        print(str(minn) + " " + str(maxx))
