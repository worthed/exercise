'''
插入排序

通过重复地将一个新元素插入到一个已安排好序的子列表中，直到整个列表排好序
'''

def insertionSort(lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1

        lst[k + 1] = currentElement