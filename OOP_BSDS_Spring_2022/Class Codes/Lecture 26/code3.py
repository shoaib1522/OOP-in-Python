def my_fun(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}, {value}')
    print ('---------------')

my_fun()
my_fun(first=1, second=2)
my_fun(day=21, month='November', year=2022)
