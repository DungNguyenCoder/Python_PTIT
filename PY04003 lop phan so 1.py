def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def ToiGian(self):
        k = gcd(self.mau, self.tu)
        self.tu //= k
        self.mau //= k
        return self
    def __str__(self):
        return f'{self.tu}/{self.mau}'

tu, mau = map(int, input().split())
phanso = PhanSo(tu, mau)
phanso.ToiGian()
print(phanso)