
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rectangle_1 = Rectangle(25, 10)
area = rectangle_1.compute_area()
print(area)