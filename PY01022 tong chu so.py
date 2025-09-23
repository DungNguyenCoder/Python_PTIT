def tong(s):
    n = 0
    for chu in s:
        n += ord(chu) - ord('0')
    return str(n)

s = input()

d = 0
while len(s) > 1:
    s = tong(s)
    d += 1
print(d)