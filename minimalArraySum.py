# Divide elements of an array by 2 for fixed no. of times (each element once during a iteration) to get minimal sum
import math;
def minSum(num, k):
    num.sort(reverse = True)

    num.insert(0,0)
    num.insert(len(num),0)


    counter = 0
    index = 1

    while (counter < k):
        print(num)
        if (num[index] >= num[index+1]) and (num[index] >= num[index-1]):
            num[index] = math.ceil((num[index]) / 2)
            counter+=1
        elif  (num[index] < num[index-1]):
            index -= 1
        else:
            index+= 1



    print(num)
    return sum(num)



print(minSum([50,10,7],10))
