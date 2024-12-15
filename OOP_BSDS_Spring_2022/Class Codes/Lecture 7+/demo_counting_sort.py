import random as r

def counting_sort(x, max_element):  #assuming values starts from 0 and ends on max_element
    counts = [0 for i in range(max_element+1)]
    for i in range(len(x)):
        counts[x[i]] += 1
    k = 0
    for i in range(len(counts)):
        for j in range(counts[i]):
            x[k] = i
            k  += 1


def demo_counting_sort():
    size = r.randint(15, 20)
    x = [ r.randint(0,6) for i in range(size)]
    print(x)
    counting_sort(x, 6)
    print(x)


demo_counting_sort()



