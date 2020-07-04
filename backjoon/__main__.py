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


a = int(input())

star1(a)
