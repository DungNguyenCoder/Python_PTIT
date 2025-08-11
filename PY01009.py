s = input()
cntLower = 0
cntUpper = 0
for ch in s:
    if ch.islower():
        cntLower += 1
    else:
        cntUpper += 1
if cntLower >= cntUpper:
    s = s.lower()
else:
    s = s.upper()
print(s)