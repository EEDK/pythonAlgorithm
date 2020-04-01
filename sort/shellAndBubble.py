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

def swap ( x , i , j) :
    x[i] , x[j] = x[j] , x[i]

def pivotFirst(x , lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark

    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x , lmark , rmark)
            lmark += 1
            rmark -= 1
    swap(x , pivot_idx, rmark)
    return rmark

def quickSort(x , pivotMethod=pivotFirst):
    def _qsrot(x, first, last):
        if first < last :
            splitpoint = pivotMethod(x, first, last)
            _qsrot(x, first, splitpoint - 1)
            _qsrot(x, splitpoint + 1 , last)
    _qsrot(x, 0 , len(x) - 1 )
