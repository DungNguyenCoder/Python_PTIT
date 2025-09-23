t = int(input())

def DoiCoSo(n, base):
    ky_tu = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = ky_tu[n % base] + res
        n //= base
    return res

for _ in range(t):
    n, coSo = map(int, input().split())
    print(DoiCoSo(n, coSo))