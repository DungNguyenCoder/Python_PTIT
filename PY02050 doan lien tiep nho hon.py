t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    st = []
    res = [0] * n
    for i in range(n):
        while st and a[st[-1]] <= a[i]:
            st.pop()
        if not st:
            res[i] = i + 1
        else:
            res[i] = i - st[-1]
        st.append(i)
    print(*res)
    print()