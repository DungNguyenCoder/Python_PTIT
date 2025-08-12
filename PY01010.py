t = int(input())

for _ in range(t):
    s = input()
    last = int(s[-2:])
    first = int(s[:2])
    if last == first:
        print("YES")
    else:
        print("NO")