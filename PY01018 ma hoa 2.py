p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    vao = input()
    cnt = len(vao.split())
    if cnt == 1 and vao == str(0):
        break
    k, s = vao.split()
    k = int(k)
    chars = list(s)
    for i in range(len(chars)):
        pos = p.index(chars[i])
        chars[i] = p[(pos + k) % 28]
    s = "".join(chars[::-1])
    print(s)
