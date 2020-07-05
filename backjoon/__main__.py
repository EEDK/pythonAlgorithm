def Sum(a , b) :
    ans = a + b 
    return ans

def Mul(a , b) :
    ans = a * b
    return ans

def star1(n):
    if n == 0:
        return
    else:
        i = 0
        while i < n:
            print('*', end='')
            i += 1
        print()
        star1(n - 1);


def star2(n):
    i = 0
    while i < n :
        j = 0
        while j < n:
            if i > j :
                print(' ', end='')
            else :
                print('*', end='')
            j += 1;
        print()
        i += 1;


a = int(input())

star2(a)
