import random as r

#function to find sum of x & y in the list, where x+y has largest sum and x, y can exist at any index
def find_max_sum_pair(list, x=0, y = 1):
    if x == len(list)-1:    return 0   #No pair return, so return 0, in case having positive elements
    if y == len(list):
        return find_max_sum_pair(list, x+1, x+2)
    sum1 = list[x]+list[y]                  #sum of current pair
    sum2 = find_max_sum_pair(list, x, y+1)  #max sum returned by the recursive call
    if sum1 > sum2: return sum1
    return sum2

def main():
    x = [r.randint(1,9) for i in range(5)]
    print (x)
    print (f'Maximum Pair Sum: {find_max_sum_pair(x)}')

main()

