class Rectangle:
    def __init__(self, x, y , colour):
        self.x = x
        self.y = y
        self.colour = colour
    def perimeter(self):
        return 2 * (self.x + self.y)
    def area(self):
        return self.x * self.y
    def color(self):
        return self.colour.capitalize()

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))