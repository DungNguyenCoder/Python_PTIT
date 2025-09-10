import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def check(self):
        A = self.a.distance(self.b)
        B = self.b.distance(self.c)
        C = self.c.distance(self.a)
        if max(A, B, C) * 2 >= A + B + C:
            return "INVALID"
        else:
            tmp = A + B + C
            s = f'{tmp:.3f}'
            return s
arr = []
t = int(input())
for x in range(t):
    arr += [float(i) for i in input().split()]
i = 0
for index in range(t):
    PointA = Point(arr[i], arr[i+1])
    PointB = Point(arr[i+2], arr[i+3])
    PointC = Point(arr[i+4], arr[i+5])
    TamGiac = Triangle(PointA, PointB, PointC)
    print(TamGiac.check())
    i += 6
