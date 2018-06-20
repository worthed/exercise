# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/4 下午10:31
IDE：PyCharm
描述：创建属于自己的迭代器
"""

# 接受一个可迭代的数字，并在循环结束时提供每个数字的平方
class square_all:
    def __init__(self, numbers):
        self.numbers = iter(numbers)

    def __next__(self):
        return next(self.numbers) ** 2

    def __iter__(self):
        return self

from itertools import count
# 我们有一个无限长的可迭代对象count，你可以看到 square_all 接受 count 而不用完全循环遍历这个无限长的迭代
numbers = count(5)
squares = square_all(numbers)

# 直接从可迭代对象中的某一部分开始遍历，而不用从头开始遍历，很节省时间和cpu
print(next(squares))
print(next(squares))

'''
但是通常不使用上述的处理方式，而是使用生成器函数
def square_all(numbers):
    for n in numbers:
        yield n**2
'''