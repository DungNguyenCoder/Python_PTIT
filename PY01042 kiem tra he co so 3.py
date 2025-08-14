t = int(input())

for _ in range(t):
    s = input()
    flag = True
    for c in s:
        if c != '1' and c != '2' and c != '0':
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")