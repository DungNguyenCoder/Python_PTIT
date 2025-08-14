def towerOfHanoi(n, a, b, c):
    if n == 1:
        print(str(a) + " -> " + str(c))
        return
    towerOfHanoi(n - 1, a, c, b)
    print(str(a) + " -> " + str(c))
    towerOfHanoi(n - 1, b, a, c)

n = int(input())
towerOfHanoi(n, 'A', 'B', 'C')