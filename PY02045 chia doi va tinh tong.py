s = input()

while len(s) != 1:
    tmp1 = int(s[0:len(s) // 2])
    tmp2 = int(s[len(s) // 2:])
    sum = tmp1 + tmp2
    s = str(sum)
    print(s)
