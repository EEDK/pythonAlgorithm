import sys

def sol(a , b , c , d , e):
    if a < 100 or a > 2000 or b < 100 or b > 2000 or  c < 100 or c > 2000 or  d < 100 or d > 2000 or  e < 100 or e > 2000:
        return -1
    gaguk_ham = sorted([a , b , c ])
    gaguk_em = sorted([d , e])

    return gaguk_ham[0] + gaguk_em[0] - 50

a = [0]*5
i = 0
for i in range(i,5) :
    a[i] = int(sys.stdin.readline())

ans = sol(a[0] , a[1], a[2] , a[3], a[4])

if ans == -1:
    print('err')
else :
    print(ans)