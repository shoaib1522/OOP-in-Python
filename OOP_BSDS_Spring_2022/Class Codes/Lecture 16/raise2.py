def find_index(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    raise 'something'

def main():
    x = [23,45,19,68]
    print (find_index(x, 19))
    print (find_index(x, 91))

main()
