import math

class Shape:
    def __init__(self, radius):
        self.radius = radius


class Circle(Shape):
    def cal_area(self):
        return math.pi * self.radius ** 2


class Sphere(Shape):
    def cal_volume(self):
        return (4/3) * math.pi * self.radius ** 3


r = float(input("Enter radius: "))

c = Circle(r)
s = Sphere(r)

print("Area of Circle =", c.cal_area())
print("Volume of Sphere =", s.cal_volume())