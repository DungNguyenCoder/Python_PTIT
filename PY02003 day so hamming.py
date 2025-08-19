def gen_hamming(limit=10**18):
    hamming = [1]
    i2 = i3 = i5 = 0
    while True:
        nxt = min(hamming[i2]*2, hamming[i3]*3, hamming[i5]*5)
        if nxt > limit:
            break
        hamming.append(nxt)
        if nxt == hamming[i2]*2: i2 += 1
        if nxt == hamming[i3]*3: i3 += 1
        if nxt == hamming[i5]*5: i5 += 1
    return hamming

hamming = gen_hamming()

pos = {}
for idx, val in enumerate(hamming):
    pos[val] = idx + 1

t = int(input())
for _ in range(t):
    n = int(input())
    if n in pos:
        print(pos[n])
    else:
        print("Not in sequence")