class ThiSinh:
    def __init__(self, name, birth, score1, score2, score3):
        self.name = name
        self.birth = birth
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    def TongDiem(self):
        s = self.score1 + self.score2 + self.score3
        return f'{s:.1f}'
    def __str__(self):
        return self.name + " " + str(self.birth) + " " + str(self.TongDiem())

name = input()
birth = input()
score1 = float(input())
score2 = float(input())
score3 = float(input())
thisinh = ThiSinh(name, birth, score1, score2, score3)
print(thisinh)
