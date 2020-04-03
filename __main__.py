from math import log10
from random import randint

global counter

def selected_sort(random_list):
    for sel in range ( len(random_list) - 1) :
        min = random_list[sel]
        minindex = sel

        for step in range( sel + 1 , len(random_list)) :
            if min > random_list[step]:
                min = random_list[step]
                minindex=step

        random_list[minindex] = random_list[sel]
        random_list[sel] = min

def binary_search(a_list , wanted_data) :
    global counter
    first = 0
    last = len(a_list) - 1

    while first <= last:
        idx = (first + last) // 2
        counter += 1
        if a_list[idx] == wanted_data:
            print('{item} found at position {i}'.format(item=wanted_data, i = idx))
            return True
        elif a_list[idx] > wanted_data:
            last = idx - 1
        elif a_list[idx] < wanted_data:
            first = idx + 1
        else:
            print('{item} not found in the list'.format(item=wanted_data))
            return False

if __name__ == '__main__':
    data = []
    counter = 0
    n = int(input("정렬할 데이터의 수 : "))
    data = [ randint(1, 100) for x in range(n)]

    print("정렬 전")
    print(data)

    selected_sort(data)

    print("정렬 후")
    print(data)

    msg = binary_search(data, 50)
    if msg == True:
        print("총 {}번의 비교만으로 {}을 검색하였습니다.".format(counter, 50))
    print(msg)