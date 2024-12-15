from point import *
class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z

    def __str__(self):
        return f'{Point.__str__(self)} \t Z: {self.z}\n'

    def __del__(self):
        Point.__del__(self)
        print (f'\tZ:  {self.z}')

def main():
    p = Point3D(2, 5, 3)
    print(p)

main()

