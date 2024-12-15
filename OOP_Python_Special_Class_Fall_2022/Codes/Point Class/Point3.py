class Point:
    def __init__(self, x, y):
        self.__x = x        #data members are private, being started with __
        self.__y = y

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'X: ' + str(self.__x) + '\tY:' + str(self.__y)

def main():
    p1 = Point(2, 3)
    p2 = Point(4, 1)
    print(p1)       #automatically __str__ function will be called
    print(p2)

main()

