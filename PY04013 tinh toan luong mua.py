from datetime import datetime

class LuongMua:
    def totalTime(self):
        t1 = datetime.strptime(self.timeStart, '%H:%M')
        t2 = datetime.strptime(self.timeEnd, '%H:%M')
        diff = t2 - t1
        return diff.seconds / 3600

    def __init__(self, name, timeStart, timeEnd, rainAmount):
        self.maTram = None
        self.name = name
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.rainAmount = rainAmount
        self.time = self.totalTime()
        self.rainAvarage = None

    def setMaTram(self, maTram):
        self.maTram = maTram

    def setAvarage(self):
        if self.time > 0:
            self.rainAvarage = self.rainAmount / self.time
        else:
            self.rainAvarage = 0

    def __str__(self):
        return f'{self.maTram} {self.name} {self.rainAvarage:.2f}'

t = int(input())
ds = {}

for i in range(t):
    name = input()
    timeStart = input()
    timeEnd = input()
    rainAmount = int(input())
    luongMua = LuongMua(name, timeStart, timeEnd, rainAmount)

    if name in ds:
        obj = ds[name]
        obj.time += luongMua.time
        obj.rainAmount += luongMua.rainAmount
    else:
        luongMua.setMaTram(f"T{i + 1 :02d}")
        ds[name] = luongMua

ds_list = list(ds.values())

for d in ds_list:
    d.setAvarage()

ds_list.sort(key=lambda x : x.maTram)
for d in ds_list:
    print(d)