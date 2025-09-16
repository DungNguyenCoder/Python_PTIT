from sys import flags

id = 1
class NhanVien:
    def __init__(self, name, lyThuyet, thucHanh):
        global id
        self.maNhanVien = "TS0"
        self.maNhanVien += str(id)
        id += 1
        self.name = name
        self.lyThuyet = self.DinhDangSo(lyThuyet)
        self.thucHanh = self.DinhDangSo(thucHanh)
        self.trungBinh = (self.lyThuyet + self.thucHanh) / 2.0
        self.xepHang = self.XepHang()

    def DinhDangSo(self, input):
        if input > 10:
            return input / 10
        else:
            return input

    def XepHang(self):
        if self.trungBinh < 5:
            return "TRUOT"
        elif self.trungBinh < 8:
            return "CAN NHAC"
        elif self.trungBinh < 9.5:
            return "DAT"
        else:
            return "XUAT SAC"

    def __str__(self):
        return f'{self.maNhanVien} {self.name} {self.trungBinh :.2f} {self.xepHang}'


t = int(input())
ds = []
for i in range(t):
    name = input()
    lyThuyet = float(input())
    thucHanh = float(input())
    nhanVien = NhanVien(name, lyThuyet, thucHanh)
    ds.append(nhanVien)

ds.sort(key=lambda x: x.trungBinh, reverse=True)
for d in ds:
    print(d)