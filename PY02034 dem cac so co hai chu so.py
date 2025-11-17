s = input()
mp = {}
if len(s) % 2 == 1:
    s = s[:-1]
n = len(s)

for i in range(0, n, 2):
    tmp = int(s[i:i + 2])
    mp[tmp] = mp.get(tmp, 0) + 1

for k, v in mp.items():
    print(k, v)
