class Point:
    def __init__(self, x=1, y=1): #parameter has default values
        self.__x = x
        self.__y = y

    def set(self, x, y):
        if x < 0:
            x = 1
        if y < 0:
            y = 1
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'X: ' + str(self.__x) + '\tY:' + str(self.__y)

def main():
    p1 = Point(3, 1)
    p2 = Point(5, 3)
    print(p1)
    print(p2)
    p1.set(-3, 4)
    p2.set(7, -4)
    print(p1)
    print(p2)

main()

