import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x0 = self.x - other.x
        y0 = self.y - other.y
        return math.sqrt(x0 * x0 + y0 * y0)

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
            tmp = math.sqrt((A + B + C) * (A + B - C) * (A - B + C) * (-A + B + C)) / 4
            s = f'{tmp:.2f}'
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
