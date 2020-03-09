# Find the missing element in a given permutation.
def solution(A):
    B = A
    B.sort()

    arraySum = sum(B)
    expectedSum = sum(range(1,B[len(B)-1]+1))


    return(expectedSum - arraySum)

print(solution([2,3,1,5]))
