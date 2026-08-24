import math

class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


class EquilateralTriangle(Triangle):
    def cal_area(self):
        return (math.sqrt(3) / 4) * self.side1 ** 2

    def find_tangent(self):
        print("Tangent of angle 1 =", math.tan(math.radians(self.angle1)))
        print("Tangent of angle 2 =", math.tan(math.radians(self.angle2)))
        print("Tangent of angle 3 =", math.tan(math.radians(self.angle3)))


t = EquilateralTriangle(6, 6, 6, 60, 60, 60)

print("Area =", t.cal_area())
t.find_tangent()