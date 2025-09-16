id = 1
class HoaDon:
    def __init__(self, name, chiSoCu, chiSoMoi):
        global id
        self.maHoaDon = "KH"
        self.maHoaDon += '{:02d}'.format(id)
        id += 1
        self.name = name
        self.chiSoCu = chiSoCu
        self.chiSoMoi = chiSoMoi
        self.thanhTien = self.calMoney()

    def calMoney(self):
        sum = self.chiSoMoi - self.chiSoCu
        thanhTien = 0.0
        if sum <= 50:
            thanhTien = sum * 100 * 1.02
        elif sum <= 100:
            thanhTien = (50 * 100 + (sum - 50) * 150) * 1.03
        else:
            thanhTien = (50 * 100 + 50 * 150 + (sum - 100) * 200) * 1.05
        return round(thanhTien)

    def __str__(self):
        return f'{self.maHoaDon} {self.name} {self.thanhTien}'

t = int(input())
ds = []
for i in range(t):
    name = input()
    chiSoCu = int(input())
    chiSoMoi = int(input())
    hoaDon = HoaDon(name, chiSoCu, chiSoMoi)
    ds.append(hoaDon)

ds.sort(key=lambda x : -x.thanhTien)
for hoaDon in ds:
    print(hoaDon)
