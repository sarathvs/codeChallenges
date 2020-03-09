# Find maximum number that can be formed using digits of a given number

def solution(N):
    stringN = str(N)
    countList = [0]* 10
    maxValue = 0

    for i in range(len(stringN)):
        countList[int(stringN[i])] += 1

    mutiplicationFactor = 1

    for j in range(10):
        while countList[j] > 0:
            value = j * mutiplicationFactor
            countList[j] = countList[j] - 1
            maxValue = maxValue + value
            mutiplicationFactor = mutiplicationFactor * 10


    return maxValue

print(solution(38293367))
