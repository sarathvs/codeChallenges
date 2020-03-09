#  Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.

def solution(N, A):
    counters = [0] * N

    for i in range(0,len(A)):
        if A[i] > N:
            counters = [max(counters)] * N
        else:
            counters[A[i] -1] += 1

    return counters

print(solution(100000, [3,2,4,5,6,6,7,10,10,100000,100000]))
