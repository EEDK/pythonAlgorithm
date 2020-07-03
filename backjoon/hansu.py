import sys

def HansuTail(n , acc) :
    if n == 1:
        return acc
    else :
        strN = str(n)
        lenN = len(strN)
        if lenN == 1 or lenN == 2:
            return HansuTail(n - 1, acc + 1)
        else :
            tempDiff = int(strN[1]) - int(strN[0])
            i = 2
            while i < lenN:
                tem = int(strN[i]) - int(strN[i-1])
                if(tem == tempDiff):
                    i += 1
                else:
                    return HansuTail(n - 1, acc)
            return HansuTail(n - 1, acc + 1)


def Hansu(n):
    return HansuTail(n , 1)

sys.setrecursionlimit(2000)
a = list(map(int, sys.stdin.readline().split()))
if(a[0] > 1000 or a[0] < 1):
    print("input err")
else :
    print(Hansu(a[0]))
