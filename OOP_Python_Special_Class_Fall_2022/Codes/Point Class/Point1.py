class Point:
    def __init__(self, x, y):
        self.__x = x        #data members are private, being started with __
        self.__y = y

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def display(self):
        print (f'X: {self.__x}\tY:{self.__y}')

def main():
    p1 = Point(2, 3)
    p2 = Point(4, 1)
    p1.display()
    p2.display()
    p2.set(20, 30)
    print('\tValue after modification in p2 only')
    p1.display()
    p2.display()

main()

