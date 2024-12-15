def print_alphabet(n):
    for i in range(n):
        print(chr(i+65),end='')
    print()
    for i in range(n):
        print(chr(i+97),end='')
    print()
    
def main():
    n = int(input())
    print_alphabet(n)
    
main()
