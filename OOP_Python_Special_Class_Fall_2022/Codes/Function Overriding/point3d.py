from point import *
class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z

    def set(self, x, y, z):
        Point.set(self, x, y)
        self.z = z

    def __str__(self):
        return f'{Point.__str__(self)} \t Z: {self.z}\n'


def main():
    p = Point3D(2, 5, 3)
    print(p)            #str of Point3D class will be called
    p.set(1, 2, 3)
    print(p)

    p1 = Point(2, 6)
    print(p1)           #str of Point class will be called
main()

