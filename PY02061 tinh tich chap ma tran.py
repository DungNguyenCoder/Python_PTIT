import sys
data = list(map(int, sys.stdin.read().split()))
it = iter(data)

t = next(it)
out = []

for _ in range(t):
    N = next(it); M = next(it)
    A = [[next(it) for _ in range(M)] for _ in range(N)]
    K = [[next(it) for _ in range(3)] for _ in range(3)]

    total = 0
    k00,k01,k02 = K[0]
    k10,k11,k12 = K[1]
    k20,k21,k22 = K[2]

    for i in range(1, N-1):
        Ai1, Ai, Ai1p = A[i-1], A[i], A[i+1]
        for j in range(1, M-1):
            s = (Ai1[j-1]*k00 + Ai1[j]*k01 + Ai1[j+1]*k02 +
                 Ai[j-1]*k10  + Ai[j]*k11  + Ai[j+1]*k12 +
                 Ai1p[j-1]*k20+ Ai1p[j]*k21+ Ai1p[j+1]*k22)
            total += s
    out.append(str(total))

sys.stdout.write("\n".join(out))
