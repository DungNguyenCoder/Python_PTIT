n, m = map(int, input().split())
a = list(map(int, input().split()))

mp = {}

for x in a:
    mp[x] = mp.get(x, 0) + 1
sorted_mp = sorted(mp.items(), key = lambda x : x[1], reverse = True)
maxx = sorted_mp[0][1]
flag = False
ans = 0
for x in sorted_mp:
    if x[1] < maxx:
        flag = True
        ans = x[0]
        break
if flag:
    print(ans)
else:
    print("NONE")
