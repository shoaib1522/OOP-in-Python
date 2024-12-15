class Rational:
    def __init__(self, n, d):
        self.__num = n
        self.__den = d

    def set(self, n, d):
        self.__num = n
        self.__den = d

    def __str__(self):
        return str(self.__num) + ' / ' + str(self.__den)

    def __add__(self, other):
        p_new = Rational(1, 1)
        p_new.__den = self.__den * other.__den
        p_new.__num = self.__num * other.__den + self.__den * other.__num
        return p_new

    def __eq__ (self, other):
        return self.__den == other.__den and self.__num == other.__num



def main():
    p1 = Rational(3, 4)
    p2 = Rational(2, 5)
    print(p1)
    print(p2)
    p3 = p1 + p2
    print(p3)
    p4 = Rational(3, 4)
    if p1 == p4:    print('P1 and P4 are same');
    else:           print('P1 and P4 are different');
    if p1 == p2:    print('P1 and P2 are same');
    else:           print('P1 and P2 are different');

main()

