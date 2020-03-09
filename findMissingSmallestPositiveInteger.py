

# Program to return the small positive integer missing in the sequence
def solution(A):
    sortedA = A
    sortedA.sort()
    index = 0
    size = len(sortedA)



    for i in range(size):

        if (sortedA[i] <=0):
            index+=1
            continue
        else:
            break

    if (index == size):
            return 1


    if (index == size - 1):
        if sortedA[index] > 1:
            return 1
        else:
            return 2


    for j in range(index,size):

        if (j == size - 1):
            return sortedA[j] + 1

        if (sortedA[j+1] - sortedA[j]) > 1:
                return (sortedA[j] + 1)
        else:
            continue

print(solution([-1,-2,0,1,2,2,3,4,5,6,7,8,9,0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,17]))
