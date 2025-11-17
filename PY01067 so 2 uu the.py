def to_base_3(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3
    return "".join(reversed(digits))

def is_upper_2(s):
    return s.count('2') > (len(s) / 2)

t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    i = 1
    while len(res) < n:
        tmp = to_base_3(i)
        if is_upper_2(tmp):
            res.append(tmp)
        i += 1
    for x in res:
        print(x, end=" ")
    print()
