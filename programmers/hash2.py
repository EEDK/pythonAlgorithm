def solution(answers):
    patternA = [1, 2, 3, 4, 5]
    patternB = [2, 1, 2, 3, 2, 4, 2, 5]
    patternC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ansLen = len(answers)

    personA = []
    personB = []
    personC = []

    correctA = 0
    correctB = 0
    correctC = 0

    i = 0
    while i < ansLen:
        personA.extend(patternA)
        i += 5

    i = 0
    while i < ansLen:
        personB.extend(patternB)
        i += 8

    i = 0
    while i < ansLen:
        personC.extend(patternC)
        i += 10


    for i in range(ansLen):
        if answers[i] == personA[i]:
            correctA += 1
        if answers[i] == personB[i]:
            correctB += 1
        if answers[i] == personC[i]:
            correctC += 1


    if correctA == correctB == correctC:
        return [1, 2, 3]
    elif correctA == correctB and correctA > correctC:
        return [1, 2]
    elif correctA == correctC and correctA > correctB:
        return [1, 3]
    elif correctB == correctC and correctB > correctA:
        return [2, 3]
    elif correctA > correctB and correctA > correctC:
        return [1]
    elif correctB > correctA and correctB > correctC:
        return [2]
    elif correctC > correctA and correctC > correctB:
        return [3]


print(solution([1,3,2,4,2]))