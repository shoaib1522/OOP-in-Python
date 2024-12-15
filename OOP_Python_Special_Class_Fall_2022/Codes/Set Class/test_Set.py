from Set import *

def main():
    s1 = Set()
    s1.add_element(23)
    s1.add_element(34)
    s1.add_element(12)
    s1.add_element(53)
    s1.add_element(34)
    print('S1: ', s1)
    s2 = Set()
    s2.add_element(16)
    s2.add_element(11)
    s2.add_element(23)
    print('S2: ', s2)
    s1.add_set(s2)
    print('S1 + S2: ', s1)

main()
