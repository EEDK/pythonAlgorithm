def Question12(n):
    i = 1
    sum = 0
    while i <= n:
        if n % i == 0:
           sum += i
        i += 1

    print(sum)

Question12(20)