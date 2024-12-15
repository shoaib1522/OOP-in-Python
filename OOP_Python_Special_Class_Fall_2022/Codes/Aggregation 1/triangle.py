from point import *

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)

    def __str__(self):
        return 'Triangle:- \n\tPoint1:' + str(self.p1) + '\tPoint2: ' + str(self.p2) + '\tPoint3: '+ str(self.p3)

    def __del__(self):
        print (f'del function called for Triangle')

def main():
    t = Triangle(2,3,7,8,5,4)
    print(t)

main()
