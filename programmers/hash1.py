"""def solution(participant, completion):
    answer = ''

    lenParticipant = len(participant)
    lenCompletion = len(completion)

    i = 0
    while i < lenParticipant:
        j = 0
        while j < lenCompletion:
            if participant[i] == completion[j]:
                completion.pop(j)
                lenCompletion -= 1
                break
            elif j == lenCompletion - 1:
                answer = participant[i]
            j += 1
        i += 1

    return answer
"""

def solution(participant, completion):

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[i+1]

a1 = ["mislav", "stanko", "mislav", 'ana']
b1 =["stanko", "ana", 'mislav']

print(solution(a1, b1))