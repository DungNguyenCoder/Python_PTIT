def gen(A: str):
    nums = [A]
    for i, ch in enumerate(A):
        if ch == '?':
            next_nums = []
            for s in nums:
                for d in '0123456789':
                    tmp = list(s)
                    tmp[i] = d
                    new_s = ''.join(tmp)
                    next_nums.append(new_s)
            nums = next_nums
    res = []
    for s in nums:
        try:
            # bỏ qua số có nhiều chữ số nhưng bắt đầu bằng '0'
            if len(s) > 1 and s[0] == '0':
                continue
            res.append(int(s))
        except:
            pass
    return res


t = int(input())
for _ in range(t):
    line = input().strip()
    parts = line.split()
    if len(parts) != 5 or parts[3] != '=':
        print("WRONG PROBLEM!")
        continue

    A, op, B, eq, C = parts
    operators = ['+', '-', '*', '/'] if op == '?' else [op]
    solved = False

    for real_op in operators:
        listA = gen(A)
        listB = gen(B)
        listC = gen(C)

        for a in listA:
            for b in listB:
                for c in listC:
                    ok = False
                    if real_op == '+':
                        ok = (a + b == c)
                    elif real_op == '-':
                        ok = (a - b == c)
                    elif real_op == '*':
                        ok = (a * b == c)
                    elif real_op == '/':
                        if b != 0 and a % b == 0:
                            ok = (a // b == c)
                    if ok:
                        print(f"{a} {real_op} {b} = {c}")
                        solved = True
                        break
                if solved:
                    break
            if solved:
                break
        if solved:
            break
    if not solved:
        print("WRONG PROBLEM!")
