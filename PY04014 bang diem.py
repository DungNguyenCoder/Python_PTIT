from decimal import Decimal, ROUND_HALF_UP

id = 0
class BangDiem:

    def __init__(self, name, hs_list):
        global id
        id += 1
        self.name = name
        self.hs_list = hs_list
        sum = self.hs_list[0] * 2 + self.hs_list[1] * 2
        for idx in range(2, 10):
            sum += self.hs_list[idx]
        sum /= 12
        self.totalScore = sum.quantize(Decimal('0.1'), ROUND_HALF_UP)
        self.xepHang = self.setXepHang()
        self.maHocSinh = "HS"
        self.maHocSinh += '{:02d}'.format(id)

    def setXepHang(self):
        if self.totalScore >= 9:
            return "XUAT SAC"
        elif self.totalScore >= 8:
            return "GIOI"
        elif self.totalScore >= 7:
            return "KHA"
        elif self.totalScore >= 5:
            return "TB"
        else:
            return "YEU"

    def __str__(self):
        return f'{self.maHocSinh} {self.name} {self.totalScore} {self.xepHang}'


t = int(input())
ds = []
for i in range(t):
    name = input()
    hs_list = [Decimal(x) for x in input().split()]
    bd = BangDiem(name, hs_list)
    ds.append(bd)

ds.sort(key=lambda x : (-x.totalScore, x.maHocSinh))

for bd in ds:
    print(bd)