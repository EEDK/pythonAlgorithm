import sys

def solve(h , m):
    if m - 45 < 0 :
        if h - 1 < 0:
            print(h + 23, end=" ")
        else :
            print(h - 1 , end =" ")
        print(m + 15)
    else:
        print(h , end =" ")
        print(m - 45)

a = list(map(int, sys.stdin.readline().split()))
solve(a[0] , a[1])