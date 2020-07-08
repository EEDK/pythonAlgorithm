import sys

g = lambda x , y : x + y
a = list(map(int, sys.stdin.readline().split()))

i = 0

while i < a[0]:
    b = list(map(int, sys.stdin.readline().split()))
    print(g(b[0] , b[1]))
    i += 1

