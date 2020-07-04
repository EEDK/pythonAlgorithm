def star1(n):
    if n == 0:
        return
    i = 0
    while i < n:
        print('*', end='')
        i += 1
    print()
    star1(n-1);


