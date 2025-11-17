import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    a = [0] + list(map(int, input().split()))  # index từ 1

    coef = [0] * (K + 1)
    for j in range(1, K + 1):
        coef[j] = j if j % 2 == 1 else -j

    # DP array
    dp = [[-10 ** 30] * (N + 1) for _ in range(K + 1)]

    # dp[0][i] = 0 nghĩa là chưa chọn gì → giá trị 0
    for i in range(N + 1):
        dp[0][i] = 0

    for j in range(1, K + 1):
        for i in range(1, N + 1):
            # không chọn i
            dp[j][i] = dp[j][i - 1]
            # chọn i
            dp[j][i] = max(dp[j][i], dp[j - 1][i - 1] + coef[j] * a[i])

    print(dp[K][N])
