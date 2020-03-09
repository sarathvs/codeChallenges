#Find value that occurs in odd number of elements.

def solution(A):
    A.sort()

    arraySize = len(A)

    if arraySize == 0:
        return "invalid array"

    if arraySize == 1:
        return A[0]


    i = 0
    while (i < arraySize-1):

        if A[i] != A[i+1]:
            return A[i]

        i = i + 2

    if i == (arraySize-1):
        return A[i]

print(solution([9,3,9,3,9,7,9]))
