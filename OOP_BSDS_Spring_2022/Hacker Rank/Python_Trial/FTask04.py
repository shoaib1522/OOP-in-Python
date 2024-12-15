def check_number(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        print(n, "is Crunchy")
    else:
        print(n, "is Ok but not Crunchy")
        
def main():
    n = int(input())
    check_number(n)
    
main()
