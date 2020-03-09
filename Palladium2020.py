# What is the minimum total area of at most two banners which cover all of the buildings?

def solution(H):
    prevBanner1 = 0
    prevBanner2 = 0
    finalBanner1 = 0
    finalBanner2 = 0
    singleBanner = 0

    for i in range(len(H)-1):
        prevBanner1 = sorted(H[0: i+1])[-1] * len(H[0: i+1])
        prevBanner2 = sorted(H[i+1: len(H)])[-1] * len(H[i+1: len(H)])

        if (finalBanner1 == 0):
            finalBanner1 = prevBanner1
            finalBanner2 = prevBanner2
        else:
            if (finalBanner1 + finalBanner2) > (prevBanner1 + prevBanner2):
                finalBanner1 = prevBanner1
                finalBanner2 = prevBanner2



    singleBanner = max(H) * len(H)

    if (finalBanner1 == 0):
        return singleBanner
    else:
        if singleBanner < (finalBanner1 + finalBanner2):
            return singleBanner
        else:
            return (finalBanner1 + finalBanner2)


print(solution([1,3,4]))
