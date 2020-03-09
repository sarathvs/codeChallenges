# Rotate an array to the right by a given number of steps.

def solution(A, K):
    B = A
    if len(B) == 0:
        return B
    for i in range(K):
        lastElement = B.pop()
        B.insert(0,lastElement)

    return B




print(solution([1,2,3,1], 2))
