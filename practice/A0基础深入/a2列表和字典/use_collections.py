# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/10/28 下午8:29
IDE：PyCharm
描述：使用python的collections模块替代内建容器类型
deque：增强功能的类似list类型
(列表是基于数组实现的，而deque是基于双链表的，所以后者在中间or前面插入元素，或者删除元素都会快很多)
defaultdict：类似dict类型
(defaultdict为新的键值添加了一个默认的工厂，可以避免编写一个额外的测试来初始化映射条目，比dict.setdefault更高效)
namedtuple：类似tuple类型
"""

from collections import defaultdict
data = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# use  setdefault
result1 = {}
data1 = [("p", 1), ("p", 2), ("p", 3),
        ("h", 1), ("h", 2), ("h", 3)]
for (key, value) in data1:
    result1.setdefault(key, []).append(value)
print(result1)


# use defaultdict 性能更好
data2 = [("p", 1), ("p", 2), ("p", 3),
        ("h", 1), ("h", 2), ("h", 3)]
result2 = defaultdict(list)
for (key, value) in data2:
    result2[key].append(value)

print(result2)