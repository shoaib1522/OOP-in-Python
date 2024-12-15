class Point:
    count = 0
    def __init__(self, x=1, y=1): #parameter has default values
        self.__x = x
        self.__y = y
        Point.count += 1

    def set(self, x, y):
        if x < 0:
            x = 1
        if y < 0:
            y = 1
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'X: ' + str(self.__x) + '\tY:' + str(self.__y)

    def __del__(self):
        Point.count -= 1


def test_function():
    p1 = Point(1, 1)
    p2 = Point(2, 2)
    p3 = Point(3, 3)
    print(f'Number of objects including objects created in test function: {Point.count}')

def main():
    p1 = Point(3, 1)
    p2 = Point(5, 3)
    print(p1)
    print(p2)
    p1.set(-3, 4)
    p2.set(7, -4)
    print(p1)
    print(p2)
    print(f'Number of objects before calling test function: {Point.count}')
    test_function()
    print(f'Number of objects after the test function: {Point.count}')
    del p1
    del p2
    print(f'Number of objects after deleting objects created in main: {Point.count}')

main()

