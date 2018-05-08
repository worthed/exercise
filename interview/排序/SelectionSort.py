'''
选择排序

选择列表中的最小元素，并将它和第一个元素交换，然后在剩余元素中选择最小值和剩余列表的第一个元素交换
'''

def selectionSort(lst):
    for i in range(len(lst) - 1):
        currentMin = lst[i]
        currentMinIndex = i

        for j in range(i + 1, len(lst)):
            if currentMin > lst[j]:
                currentMin = lst[j]
                currentMinIndex = j
        if currentMinIndex != i:
            lst[currentMinIndex] = lst[i]
            lst[i] = currentMin

lst = [1, 9, 4.5, 10.6, 5.7, -4.5]
selectionSort(lst)
