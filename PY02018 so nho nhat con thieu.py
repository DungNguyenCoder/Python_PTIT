n = int(input())

a = list(map(int, input().split()))
a.sort()
flag = False
if a[0] > 1:
    print(1)
else:
    for i in range(n - 1):
        if a[i+1] - a[i] != 1:
            flag = True
            print(a[i] + 1)
            break
    if not flag:
        print(a[n - 1] + 1)