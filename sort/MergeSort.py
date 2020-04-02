def merge_sort(list):
    if len(list) <= 1 : return list
    half = len(list) // 2
    left_list = merge_sort(list[:half])
    right_list = merge_sort(list[half:])
    merged_list = []

    while len(left_list) > 0 and len(right_list) > 0 :
        if left_list[0] > right_list[0] :
            merged_list.append(right_list[0])
            right_list.pop(0)
        else :
            merged_list.append(left_list[0])
            left_list.pop(0)
    if len(left_list) > 0 : merged_list += left_list
    if len(right_list) > 0 : merged_list += right_list
    return merged_list


def left_node(idx = None):
    return ((idx + 1) << 1) - 1

def right_node(idx = None):
    return (idx + 1) << 1

def up_heap(mylist=None, idx=None, heap_size = None):
    l_node = left_node(idx)
    r_node = right_node(idx)

    if l_node <= heap_size and mylist[l_node] > mylist[idx]:
        largest = l_node
    else:
        largest = idx
    if r_node <= heap_size and mylist[r_node] > mylist[largest]:
        largest = r_node
    if largest != idx:
        mylist[idx] , mylist[largest] = mylist[largest] , mylist[idx]
        up_heap(mylist, largest, heap_size)

def build_heap(mylist = None) :
    heap_size = len(mylist) - 1
    for i in reversed(range(len(mylist))) :
        up_heap(mylist , i , heap_size)

def heap_sort(heap=None):
    tmp_array = list()
    for i in range(len(heap)):
        tmp_array.append(heap.pop(0))
        up_heap(heap, 0 , len(heap) - 1)
    return tmp_array