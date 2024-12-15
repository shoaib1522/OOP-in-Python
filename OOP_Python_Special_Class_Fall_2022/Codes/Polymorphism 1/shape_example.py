from random import *

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

def main():
    if randint(0, 1) == 0:
        shape = Rectangle(5, 3)
    else:
        shape = Circle(2)

    print('Area: ', shape.calculate_area())

main()