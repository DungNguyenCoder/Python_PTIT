from datetime import datetime


class PlayTime:
    def __init__(self, ma, ten, gioVao, gioRa):
        self.ma = ma
        self.ten = ten
        self.gioVao = gioVao
        self.gioRa = gioRa
        t1 = datetime.strptime(self.gioVao, "%H:%M")
        t2 = datetime.strptime(self.gioRa, "%H:%M")
        self.timePlay = (t2 - t1).seconds
        self.gio = self.timePlay // 3600
        if self.timePlay % 3600 != 0:
            self.phut = (self.timePlay % 3600) // 60
        else:
            self.phut = 0

    def __str__(self):
        return f'{self.ma} {self.ten} {self.gio} gio {self.phut} phut'


t = int(input())
ds = []
for i in range(t):
    ma = input()
    ten = input()
    gioVao = input()
    gioRa = input()
    ds.append(PlayTime(ma, ten, gioVao, gioRa))

ds.sort(key=lambda x: -x.timePlay)

for d in ds:
    print(d)