n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)

mul2 = max(a[0] * a[1], a[-1] * a[-2])
mul3 = max(a[0] * a[1] * a[2], a[0] * a[-1] * a[-2], a[-1] * a[-2] * a[-3], a[0] * a[1] * a[-1])
maxx = max(mul2, mul3)
print(maxx)