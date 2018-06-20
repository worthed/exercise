# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/4 下午10:13
IDE：PyCharm
描述：python中的迭代
列表，元组和字符串都是序列，序列是可以迭代的，可以使用索引，同时迭代器是一次性的，不能重新加载和再次使用
集合、字典、文件和生成器都是可迭代的，但是它们都不是序列，不可以使用索引，如a[1]
"""

# Python 的 for 循环在底层不使用索引，使用的是迭代器
numbers = [1, 2, 3]
my_iterator = iter(numbers)  # 将一个迭代器传递给iter函数，iter函数会返回一个迭代器
# 一旦有了迭代器，就可以使用内置的next函数来获取它的下一项
print(next(my_iterator)) # 输出1
print(next(my_iterator)) # 输出2
print(next(my_iterator)) # 输出3
print(next(my_iterator)) # 报错StopIteration

# 生成器
squares = (n**2 for n in numbers)
'''
对于一个生成器，因为是生成器是迭代器，可以用next获取它的下一项 next(squares)
也可以用循环遍历 for n in squares:
因此：生成器既是迭代器，也是可迭代的，即：在 Python 中迭代器也是可迭代的，它们充当它们自己的迭代器
只是迭代器没有长度，不能使用索引

'''