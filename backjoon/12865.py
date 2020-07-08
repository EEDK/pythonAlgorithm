import sys

a = list(map(int, sys.stdin.readline().split()))
len_A = a[0]
max_W = a[1]

c = []

i = 0
while i < len_A:
    b = list(map(int, sys.stdin.readline().split()))
    print((b[0] , b[1]))
    c.append([b[0] , b[1]])
    i += 1

i = 0
while i < len_A:
    whg = c[i][0]
    sum = c[i][1]
    j = 0
    while j < len_A:
        if j == i :
            continue
        else :
            if whg + c[j][0] > max_W:
                continue
            
