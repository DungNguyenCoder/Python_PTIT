n, m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

if a == b:
    print("YES")
else:
    print("NO")
