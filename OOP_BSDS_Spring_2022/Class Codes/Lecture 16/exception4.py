def main():
    try:
        x = int(input('Enter X:'))
        y = int(input('Enter Y:'))
        print (x/y)
        print ('I also want to be printed')
    except:
        print ('something is worng')
    else:
        print ('I am in else block')
    finally:
        print ('I will be printed in any case')
main()
