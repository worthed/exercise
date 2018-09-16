# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/8/18 下午8:37
IDE：PyCharm
描述：
快速排序是在一个数组中选择一个基准值，把小于基准值的数放在左边形成一个数组，大于基准值的数放在右边形成一个数组
如果左右的数组含有2个或两个以上数，则再对该数组使用快速排序
总的来说：就是一个递归

快速排序，假如数组是有序的（8个数字从小到大依次排），选择第一个值为基准值，调用栈会进行8次，  最糟情况，大O法: O(n)
而选择中间的那个数为基准值，则需要4次  最佳情况，大O法：O(log n)
则最佳情况表示为：O(n)*O(log n) = O(nlog n )
"""
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # 选择第一个数为基准值
        less = [i for i in array[1:] if i <= pivot] # 小于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]  # 大于基准值的元素组成的子数组

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23]))



