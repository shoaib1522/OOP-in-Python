from point import *

class Polygon:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.points = []
        self.points.append(Point(x1, y1))
        self.points.append(Point(x2, y2))
        self.points.append(Point(x3, y3))

    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def remove_point(self, index):
        self.points.remove(self.points[index])
        
    def __str__(self):
        s = 'Polygon:- \n'
        for i in range(len(self.points)):
            s = s + f'\tPoint {i+1}: {str(self.points[i])}'
        return s

    def __del__(self):
        print (f'del function called for Polygon')

def main():
    p = Polygon(2,3,7,8,5,4)
    print(p)
    print('----------------')
    p.add_point(6, 1)
    p.add_point(3, -2)
    p.remove_point(1)
    print(p)
main()
