class Shape:
    def area(self):
        print("Calculating the area of a generic shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        calculated_area = 3.14 * self.radius ** 2
        print(f"The area of the circle is {calculated_area} square units.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        calculated_area = self.length * self.width
        print(f"The area of the rectangle is {calculated_area} square units.")

def main():
    shape = Shape()
    circle = Circle(5)
    rectangle = Rectangle(3, 4)

    shape.area()
    circle.area()
    rectangle.area()

main()