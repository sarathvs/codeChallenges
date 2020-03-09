def solution(n):
    binary = '{0:b}'.format(n)


    prevCount = 0
    currentCount = 0
    startOfOne = False

    for i in range(len(binary) -1):

        if (binary[i] == "1" and binary[i+1] == "1"):
            continue

        if (binary[i] == "1" and binary[i+1] == "0"):
            prevCount+=1
            startOfOne= True
            continue

        if (binary[i] == "0" and binary[i+1] == "0"):

            if (startOfOne):
                prevCount+=1
                continue

        if (binary[i] == "0" and binary[i+1] == "1"):
            if (startOfOne):
                if currentCount < prevCount:
                    currentCount = prevCount
                prevCount=0
                startOfOne=False
                continue

    return currentCount

print(solution(1376796946))
