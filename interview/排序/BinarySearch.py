'''
二分查找法

前提：列表是生序排列的，二份查找法会首先将关键字和列表的中间元素进行比较，小于，则在前半部分继续，大于，则在后半部分继续，以此类推
'''

def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1

    return -low - 1

lst = [2, 4, 7, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79]
i = binarySearch(lst, 2) # return 0
i = binarySearch(lst, 11) # return 4
i = binarySearch(lst, 12) # return -6
i = binarySearch(lst, 1) # return -1
i = binarySearch(lst, 3) # return -2