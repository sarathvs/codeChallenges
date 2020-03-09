# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
def solution(A):
    currentSum=0
    finalSum=None
    p = 0

    for p in range(1, len(A)):

        currentSum = abs(sum(A[0:p]) - sum(A[p:len(A)]))

        if (finalSum == None):
            finalSum = currentSum
        else:
            if finalSum > currentSum:
                finalSum = currentSum

    return finalSum

print(solution([3,1,2,4,3]))
