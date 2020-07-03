import sys

nanugi = lambda x , y : x / y

if __name__ == '__main__':
    a = list(map(int, sys.stdin.readline().split()))
    print(nanugi(a[0],a[1]))
