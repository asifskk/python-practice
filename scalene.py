import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


class ScaleneTriangle(Triangle):
    def cal_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def cal_area(self):
        s = self.cal_perimeter() / 2

        area = math.sqrt(
            s * (s - self.side1) *
            (s - self.side2) *
            (s - self.side3)
        )

        return area


t = ScaleneTriangle(5, 6, 7)

print("Perimeter =", t.cal_perimeter())
print("Area =", round(t.cal_area()))