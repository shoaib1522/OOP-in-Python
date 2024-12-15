import random as r

def insert_in_order(x, y, index):
    temp = x[index]
    temp_y = y[index]
    i = index - 1
    while i>=0 and x[i]>temp:
        x[i+1] = x[i]
        y[i+1] = y[i]
        i = i - 1
    x[i+1]=temp
    y[i+1]=temp_y

def insertion_sort(x, y):
    for i in range(1,len(x)):
        insert_in_order(x, y, i)

def binary_search(x, element):
    start = 0
    end = len(x) - 1
    while start <= end:
        middle = int((start + end) / 2)
        if x[middle] == element:
            return middle
        elif x[middle] > element:
            end = middle - 1
        else:
            start = middle + 1
    return -1

def demo_parallel_array1():
    size = r.randint(15, 20)
    x = [ r.randint(10,99) for i in range(size)]
    y = [ r.randint(10,99) for i in range(size)]
    print("Before Sorting:")
    print(x)
    print(y)
    insertion_sort(x, y)
    print("After Sorting:")
    print(x)
    print(y)
    while (True):
        index = binary_search(x, r.randint(10,99))
        if index != -1:
            print(f'{x[index]}, {y[index]}')
            break
    #Now making a copy of lists
    a=[0]*size
    b=[0]*size
    a=[x[i] for i in range(len(x))]
    b=[y[i] for i in range(len(y))]
    print("Before Sorting:")
    print(a)
    print(b)
    insertion_sort(b, a)
    print("After Sorting:")
    print(a)
    print(b)
    #now search in b and display corresponding element of both a & b
    while (True):
        index = binary_search(b, r.randint(10,99))
        if index != -1:
            print(f'{a[index]}, {b[index]}')
            break

demo_parallel_array1()



