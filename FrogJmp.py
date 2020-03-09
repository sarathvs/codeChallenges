# Count minimal number of jumps from position X to Y.
def solution(X, Y, D):
    numOfJumps = 0
    current = X


    distance = Y - X

    numOfJumps = distance // D

    if (distance % D) > 0:
        numOfJumps += 1

    return numOfJumps

print(solution(10, 85, 30))
