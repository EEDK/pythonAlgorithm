import random
import time
import math


def bubble_sort(list) :
    for i in range(len(list) - 1):
        for j in range(1 , len(list) - i):
            if list[j - 1] > list[j]:
                temp = list[j - 1]
                list[j - 1] = list[j]
                list[j] = temp


def shell_sort(random_list):
    h = 1
    while h < len(random_list):
        h = h * 3 + 1
    h = math.floor(h / 3)

    while h > 0:
        for i in range(h):
            start_index = i + h

            while start_index < len(random_list):
                temp = random_list[start_index]
                insert_index = start_index

                while insert_index > h - 1 and random_list[insert_index - h] > temp:
                    random_list[insert_index] = random_list[insert_index - h]
                    insert_index = insert_index - h

                random_list[insert_index] = temp
                start_index = start_index + h
        h = math.floor(h / 3)


if __name__ == '__main__':
    list = []
    n = input("정렬할 데이터 수 : ")
    for i in range(int(n)):
        list.append(random.randint(1 , int(n)))
    print("정렬 전")
    print(list)

    start_time = time.time()
    shell_sort(list)
    running_time = time.time() - start_time

    print("정렬 후")
    print(list)

    print("데이터의 크기 : {}".format(int(n)))
    print("실행 시간 : {}".format(running_time))
