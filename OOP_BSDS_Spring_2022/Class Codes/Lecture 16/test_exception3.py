def main():
    try:
        x = int(input())
        y = int(input())
        print (x/y)
        print ('I also want to be printed')
    except:
        print ('Divide by zero error')
    else:
        print ('I am in else block')
    finally:
        print ('I will always  print')

main()
