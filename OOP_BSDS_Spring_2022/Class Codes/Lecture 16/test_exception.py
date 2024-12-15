def main():
    try:
        a = int(input())
        b = int(input())
        print (a/b)
    except:
        print('Divide by zero error')
    else:
        print('In else block')
    finally:
        print('In finally block')

main()

