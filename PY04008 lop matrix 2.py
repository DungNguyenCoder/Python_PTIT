class Matrix:
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix
    def ChuyenVi(self):
        tmp = [[self.matrix[i][j] for i in range(self.n)] for j in range(self.m)]
        return Matrix(self.m, self.n, tmp)
    def Tich(self, other):
        res = [[0 for _ in range(other.m)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    res[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(self.n, other.m, res)
    def __str__(self):
        s = ""
        for i in range(self.n):
            for j in range(self.m):
                s += str(self.matrix[i][j]) + " "
            s += "\n"
        return s

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        row = []
        row.extend(map(int, input().split()))
        a.append(row)
    matrix = Matrix(n, m, a)
    chuyenvi = matrix.ChuyenVi()
    matrix = matrix.Tich(chuyenvi)
    print(matrix, end = "")