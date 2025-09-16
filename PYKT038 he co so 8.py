def DoiCoSo(n, base):
    ky_tu = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = ky_tu[n % base] + res
        n //= base
    return res

s = input()
if len(s) % 3 == 1:
    s = "00" + s
elif len(s) % 3 == 2:
    s = "0" + s
ans = ""
for i in range(0, len(s), 3):
    tmp = s[i : i + 3]
    so = int(tmp, 2)
    tmp = DoiCoSo(so, 8)
    ans += tmp
print(ans)
