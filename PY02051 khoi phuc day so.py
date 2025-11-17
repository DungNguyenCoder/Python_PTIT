n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(0)
    exit()

S01 = B[0][1]
S02 = B[0][2]
S12 = B[1][2]

A0 = (S01 + S02 - S12) // 2

A = [0]*n
A[0] = A0

for i in range(1, n):
    A[i] = B[0][i] - A0

print(*A)
