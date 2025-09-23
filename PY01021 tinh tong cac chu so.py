t = int(input())

for _ in range(t):
    s = input()
    chu = ""
    sum = 0
    for i in range(len(s)):
        if s[i].isdigit():
            sum += int(s[i])
        else:
            chu += s[i]
    chu = "".join(sorted(chu))
    print(chu + str(sum))