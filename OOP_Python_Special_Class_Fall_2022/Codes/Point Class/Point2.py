class Point:
    def __init__(self, x, y):
        self.__x = x        #data members are private, being started with __
        self.__y = y

    def set(self, x, y):
        self.__x = x
        self.__y = y

    #private method created just to demonstrate that outside access is not possible
    def __show(self):
        print (f'X: {self.__x}, Y: {self.__y}')

    def display(self):
        self.__show()

def main():
    p1 = Point(2, 3)
    p2 = Point(4, 1)
    p1.display()
    p3 = p1
    p3.display()
    p3.set(1,1)
    p1.display()


main()

