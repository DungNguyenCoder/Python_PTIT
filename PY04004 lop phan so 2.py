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
    def sum(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        phanso = PhanSo(tu, mau)
        phanso.ToiGian()
        return phanso
    def __str__(self):
        return f'{self.tu}/{self.mau}'

tu1, mau1, tu2, mau2 = map(int, input().split())
phanso1 = PhanSo(tu1, mau1)
phanso2 = PhanSo(tu2, mau2)
phanso1 = phanso1.sum(phanso2)
print(phanso1)