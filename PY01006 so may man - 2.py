t = int(input())
for _ in range(t):
    n = input()
    check = True
    for i in n:
        if not(int(i) == 4 or int(i) == 7):
            print("NO")
            check = False
            break
    if check:
        print("YES")