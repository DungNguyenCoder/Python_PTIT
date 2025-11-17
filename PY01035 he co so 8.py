def chuyen_co_so(s):
    tmp = int(s[0]) * 4 + int(s[1]) * 2 + int(s[2]) * 1
    return str(tmp)

s = input()
ans = ""

while len(s) % 3 != 0:
    s = "0" + s
for i in range(0, len(s), 3):
    s1 = s[i: i + 3]
    tmp = chuyen_co_so(s1)
    ans += tmp
print(ans)