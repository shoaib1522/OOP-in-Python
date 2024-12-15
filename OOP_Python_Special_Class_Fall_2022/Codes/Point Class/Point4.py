class Point:
    def __init__(self, x=1, y=1): #parameter has default values
        self.__x = x
        self.__y = y

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'X: ' + str(self.__x) + '\tY:' + str(self.__y)

def main():
    p1 = Point()
    p2 = Point(4)
    p3 = Point(5,3)
    print(p1)
    print(p2)
    print(p3)

main()

